"""Exception hierarchy. Messages never contain key material or plaintext."""

class SecureCryptError(Exception):
    """Base class for all SecureCrypt errors."""

class InvalidFormatError(SecureCryptError):
    """Input is not a supported SecureCrypt container."""

class AuthenticationError(SecureCryptError):
    """Wrong key/passphrase or modified ciphertext/header."""

class TruncationError(AuthenticationError):
    """Encrypted stream ended before its authenticated final chunk."""

class OperationCancelled(SecureCryptError):
    """The user cancelled a running operation."""

class AuditLogTamperedError(SecureCryptError):
    """The audit log hash chain or HMAC failed verification."""
