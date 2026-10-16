"""AEAD cipher strategies and factory for SecureCrypt."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, Dict, Type
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from .errors import AuthenticationError

KEY_SIZE = 32
NONCE_SIZE = 12
TAG_SIZE = 16

class SymmetricCipher(ABC):
    alg_id: int = 0
    name: str = ""
    description: str = ""

    def __init__(self, key: bytes) -> None:
        if not isinstance(key, (bytes, bytearray)) or len(key) != KEY_SIZE:
            raise ValueError(f"{self.name} requires a {KEY_SIZE}-byte key")
        if not any(key):
            raise ValueError("refusing to use an all-zero (empty) key")
        self._aead = self._build(bytes(key))

    @abstractmethod
    def _build(self, key: bytes): ...

    def encrypt(self, nonce: bytes, plaintext: bytes, aad: bytes | None = None) -> bytes:
        if len(nonce) != NONCE_SIZE:
            raise ValueError("bad nonce length")
        return self._aead.encrypt(nonce, plaintext, aad)

    def decrypt(self, nonce: bytes, ciphertext: bytes, aad: bytes | None = None) -> bytes:
        try:
            return self._aead.decrypt(nonce, ciphertext, aad)
        except InvalidTag as exc:
            raise AuthenticationError("authentication failed: wrong key/passphrase or the data was modified") from exc

_REGISTRY: Dict[str, Type[SymmetricCipher]] = {}
_BY_ID: Dict[int, Type[SymmetricCipher]] = {}

def register(cls: Type[SymmetricCipher]) -> Type[SymmetricCipher]:
    _REGISTRY[cls.name] = cls
    _BY_ID[cls.alg_id] = cls
    return cls

@register
class AESGCMCipher(SymmetricCipher):
    alg_id = 1
    name = "AES-256-GCM"
    description = "NIST standard; fast on CPUs with AES acceleration"
    def _build(self, key: bytes):
        return AESGCM(key)

@register
class ChaCha20Cipher(SymmetricCipher):
    alg_id = 2
    name = "ChaCha20-Poly1305"
    description = "RFC 8439; performant in software"
    def _build(self, key: bytes):
        return ChaCha20Poly1305(key)

class CipherFactory:
    @staticmethod
    def names() -> list[str]:
        return list(_REGISTRY)

    @staticmethod
    def get_class(name_or_id: str | int) -> Type[SymmetricCipher]:
        table: dict = _BY_ID if isinstance(name_or_id, int) else _REGISTRY
        try:
            return table[name_or_id]
        except KeyError:
            raise ValueError(f"unknown cipher: {name_or_id!r}") from None

    @classmethod
    def create(cls, name_or_id: str | int, key: bytes) -> SymmetricCipher:
        return cls.get_class(name_or_id)(key)

    @staticmethod
    def default_name() -> str:
        return AESGCMCipher.name

def make_cipher_builder(name_or_id: str | int) -> Callable[[bytes], SymmetricCipher]:
    klass = CipherFactory.get_class(name_or_id)
    return lambda key: klass(key)
