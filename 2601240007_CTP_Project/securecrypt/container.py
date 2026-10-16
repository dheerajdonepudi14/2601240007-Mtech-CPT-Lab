"""Version 1 SecureCrypt .scx binary container format."""
from __future__ import annotations
import struct
from dataclasses import dataclass
from .ciphers import NONCE_SIZE, TAG_SIZE
from .errors import InvalidFormatError
from .keys import SALT_SIZE, KdfParams

MAGIC = b"SCRX"
VERSION = 1
NONCE_PREFIX_SIZE = 7
FILE_ID_SIZE = 16
WRAPPED_DEK_SIZE = 32 + TAG_SIZE
CORE_FMT = ">4sBBI7s16s"
SLOT_FMT = ">BIIB16s12s48s"
CORE_SIZE = struct.calcsize(CORE_FMT)
SLOT_SIZE = struct.calcsize(SLOT_FMT)
HEADER_SIZE = CORE_SIZE + SLOT_SIZE
MAX_META_SIZE = 64 * 1024
MIN_CHUNK, MAX_CHUNK = 4 * 1024, 64 * 1024 * 1024
DEFAULT_CHUNK = 1024 * 1024
MAX_CHUNKS = 2**32 - 1

@dataclass(frozen=True)
class CoreHeader:
    alg_id: int
    chunk_size: int
    nonce_prefix: bytes
    file_id: bytes
    version: int = VERSION

    def pack(self) -> bytes:
        return struct.pack(CORE_FMT, MAGIC, self.version, self.alg_id, self.chunk_size, self.nonce_prefix, self.file_id)

    @classmethod
    def unpack(cls, raw: bytes) -> "CoreHeader":
        if len(raw) < CORE_SIZE:
            raise InvalidFormatError("file is too short to be a SecureCrypt container")
        magic, ver, alg, cs, prefix, fid = struct.unpack(CORE_FMT, raw[:CORE_SIZE])
        if magic != MAGIC:
            raise InvalidFormatError("not a SecureCrypt (.scx) file")
        if ver != VERSION:
            raise InvalidFormatError(f"unsupported container version {ver}")
        if not MIN_CHUNK <= cs <= MAX_CHUNK:
            raise InvalidFormatError("invalid chunk size in header")
        return cls(alg, cs, prefix, fid, ver)

    def chunk_nonce(self, counter: int, last: bool) -> bytes:
        if counter > MAX_CHUNKS:
            raise ValueError("file too large for one container (2^32 chunks)")
        return self.nonce_prefix + struct.pack(">IB", counter, 1 if last else 0)

@dataclass(frozen=True)
class KeySlot:
    params: KdfParams
    wrap_nonce: bytes
    wrapped_dek: bytes

    def pack(self) -> bytes:
        p = self.params
        return struct.pack(SLOT_FMT, p.kdf_id, p.p1, p.p2, p.p3, p.salt, self.wrap_nonce, self.wrapped_dek)

    @classmethod
    def unpack(cls, raw: bytes) -> "KeySlot":
        if len(raw) < SLOT_SIZE:
            raise InvalidFormatError("truncated key slot")
        kdf, p1, p2, p3, salt, wn, wd = struct.unpack(SLOT_FMT, raw[:SLOT_SIZE])
        return cls(KdfParams(kdf, p1, p2, p3, salt), wn, wd)

def wrap_aad(core: bytes, params: KdfParams) -> bytes:
    """Bind the immutable core and KDF parameters as associated data."""
    return core + b"|kek|" + struct.pack(">BIIB", params.kdf_id, params.p1, params.p2, params.p3) + params.salt

assert NONCE_PREFIX_SIZE + 5 == NONCE_SIZE and SALT_SIZE == 16
