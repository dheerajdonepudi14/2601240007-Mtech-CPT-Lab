"""SecureCrypt: authenticated file encryption utility.

Uses AEAD ciphers, envelope encryption, chunked streaming, and a
tamper-evident audit log. Secret material is not written to logs.
"""
__version__ = "1.0.0"
APP_NAME = "SecureCrypt"
FILE_EXTENSION = ".scx"
