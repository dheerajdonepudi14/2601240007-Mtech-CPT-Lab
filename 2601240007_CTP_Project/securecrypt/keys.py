"""Key management and envelope encryption for SecureCrypt."""
from __future__ import annotations
import hashlib, os, threading
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from .ciphers import KEY_SIZE, NONCE_SIZE
from .errors import AuthenticationError

try:
    from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
    HAVE_ARGON2 = True
except ImportError:
    HAVE_ARGON2 = False

SALT_SIZE = 16
KDF_ARGON2ID, KDF_PBKDF2, KDF_KEYFILE = 1, 2, 3
KDF_NAMES = {1: "Argon2id", 2: "PBKDF2-HMAC-SHA256", 3: "Keyfile (HKDF-SHA256)"}
ARGON2_PROFILES = {"interactive": (2, 19 * 1024, 1), "moderate": (3, 64 * 1024, 4), "sensitive": (4, 256 * 1024, 4)}
PBKDF2_ITERATIONS = 600_000
MIN_KEYFILE_BYTES = 32

def wipe(buf: bytearray | None) -> None:
    if buf is not None:
        for i in range(len(buf)): buf[i] = 0

def hkdf(key: bytes, info: bytes, length: int = KEY_SIZE, salt: bytes | None = None) -> bytes:
    return HKDF(algorithm=hashes.SHA256(), length=length, salt=salt, info=info).derive(key)

@dataclass(frozen=True)
class KdfParams:
    kdf_id: int
    p1: int
    p2: int
    p3: int
    salt: bytes
    def describe(self) -> str:
        if self.kdf_id == KDF_ARGON2ID: return f"Argon2id (t={self.p1}, m={self.p2 // 1024} MiB, p={self.p3})"
        if self.kdf_id == KDF_PBKDF2: return f"PBKDF2-HMAC-SHA256 ({self.p1:,} iterations)"
        return KDF_NAMES.get(self.kdf_id, f"unknown KDF #{self.kdf_id}")

class KeyManager(ABC):
    def __init__(self) -> None:
        self._cache: dict[KdfParams, bytes] = {}
        self._lock = threading.Lock()
        self._batch_params: KdfParams | None = None
    @property
    @abstractmethod
    def label(self) -> str: ...
    @abstractmethod
    def _fresh_params(self) -> KdfParams: ...
    @abstractmethod
    def _derive(self, params: KdfParams) -> bytes: ...
    @abstractmethod
    def accepts(self, params: KdfParams) -> bool: ...
    def new_params(self) -> KdfParams:
        with self._lock:
            if self._batch_params is None: self._batch_params = self._fresh_params()
            return self._batch_params
    def get_kek(self, params: KdfParams) -> bytes:
        if not self.accepts(params): raise AuthenticationError(f"this file was locked with {params.describe()}, not {self.label}")
        with self._lock:
            kek = self._cache.get(params)
            if kek is None:
                kek = self._derive(params)
                self._cache[params] = kek
            return kek
    def forget(self) -> None:
        with self._lock: self._cache.clear()

class PasswordKeyManager(KeyManager):
    def __init__(self, passphrase: str | bytes, kdf: str = "argon2id", profile: str = "moderate") -> None:
        super().__init__()
        if not passphrase: raise ValueError("passphrase must not be empty")
        self._pw = bytearray(passphrase.encode() if isinstance(passphrase, str) else passphrase)
        if kdf == "argon2id" and not HAVE_ARGON2: kdf = "pbkdf2"
        if kdf not in ("argon2id", "pbkdf2"): raise ValueError(f"unknown KDF {kdf!r}")
        if profile not in ARGON2_PROFILES: raise ValueError(f"unknown profile {profile!r}")
        self.kdf, self.profile = kdf, profile
    @property
    def label(self) -> str: return "a passphrase"
    def accepts(self, params: KdfParams) -> bool: return params.kdf_id in (KDF_ARGON2ID, KDF_PBKDF2)
    def _fresh_params(self) -> KdfParams:
        salt = os.urandom(SALT_SIZE)
        if self.kdf == "argon2id":
            t, m, p = ARGON2_PROFILES[self.profile]
            return KdfParams(KDF_ARGON2ID, t, m, p, salt)
        return KdfParams(KDF_PBKDF2, PBKDF2_ITERATIONS, 0, 0, salt)
    def _derive(self, params: KdfParams) -> bytes:
        pw = bytes(self._pw)
        if params.kdf_id == KDF_ARGON2ID:
            if not HAVE_ARGON2: raise AuthenticationError("this platform's cryptography build lacks Argon2id")
            if not (1 <= params.p1 <= 64 and 8 <= params.p2 <= 4 * 1024 * 1024 and 1 <= params.p3 <= 64):
                raise AuthenticationError("Argon2 parameters in header are out of safe bounds")
            return Argon2id(salt=params.salt, length=KEY_SIZE, iterations=params.p1, lanes=params.p3, memory_cost=params.p2).derive(pw)
        if not (10_000 <= params.p1 <= 50_000_000): raise AuthenticationError("PBKDF2 iteration count in header is out of safe bounds")
        return PBKDF2HMAC(algorithm=hashes.SHA256(), length=KEY_SIZE, salt=params.salt, iterations=params.p1).derive(pw)
    def forget(self) -> None:
        super().forget(); wipe(self._pw)

class KeyfileKeyManager(KeyManager):
    def __init__(self, keyfile: str | os.PathLike) -> None:
        super().__init__()
        data = Path(keyfile).read_bytes()
        if len(data) < MIN_KEYFILE_BYTES: raise ValueError(f"keyfile must contain at least {MIN_KEYFILE_BYTES} bytes")
        self._ikm = bytearray(data)
        self.fingerprint = hashlib.sha256(data).hexdigest()[:16]
    @property
    def label(self) -> str: return f"keyfile {self.fingerprint}"
    def accepts(self, params: KdfParams) -> bool: return params.kdf_id == KDF_KEYFILE
    def _fresh_params(self) -> KdfParams: return KdfParams(KDF_KEYFILE, 0, 0, 0, os.urandom(SALT_SIZE))
    def _derive(self, params: KdfParams) -> bytes: return hkdf(bytes(self._ikm), info=b"securecrypt/v1/kek", salt=params.salt)
    def forget(self) -> None:
        super().forget(); wipe(self._ikm)
    @staticmethod
    def generate(path: str | os.PathLike, size: int = 64) -> str:
        path = Path(path)
        if path.exists(): raise FileExistsError(f"{path} already exists")
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as fh: fh.write(os.urandom(size))
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]

def wrap_dek(kek: bytes, dek: bytes, aad: bytes) -> tuple[bytes, bytes]:
    nonce = os.urandom(NONCE_SIZE)
    return nonce, AESGCM(kek).encrypt(nonce, dek, aad)

def unwrap_dek(kek: bytes, nonce: bytes, wrapped: bytes, aad: bytes) -> bytearray:
    from cryptography.exceptions import InvalidTag
    try: return bytearray(AESGCM(kek).decrypt(nonce, wrapped, aad))
    except InvalidTag: raise AuthenticationError("wrong passphrase/keyfile, or the file header was modified") from None
