# SecureCrypt — Authenticated File Encryption

> **M.Tech CTP Project | Python | Applied Cryptography**

SecureCrypt is a Python-based file encryption utility with command-line and graphical interfaces. It is designed to demonstrate authenticated encryption, password-based key derivation, envelope encryption, secure file handling, and tamper-evident audit logging.

## Key Features

- **Authenticated encryption:** AES-256-GCM and ChaCha20-Poly1305 cipher support.
- **Password-based key derivation:** Argon2id where supported, with PBKDF2-HMAC-SHA256 fallback.
- **Keyfile support:** Generate and use a separate keyfile as an encryption credential.
- **Envelope encryption:** A randomly generated data-encryption key (DEK) is wrapped using a key-encryption key (KEK).
- **Streaming and chunked processing:** Handle files without requiring the entire file to be loaded into memory.
- **Integrity protection:** Authentication detects tampering, truncation, reordering, and invalid ciphertext.
- **Audit trail:** Hash/MAC-chained operation records help detect edits to the local audit log.
- **Batch operations:** Process multiple files through the CLI workflow.
- **Two interfaces:** Interactive terminal CLI and desktop GUI.
- **Tests:** Pytest/Hypothesis-based coverage for round trips, invalid input, tampering, and key handling.

## Project Structure

```text
2601240007_CTP_Project/
├── securecrypt/                 # Core encryption package
│   ├── cli.py                    # Command-line interface
│   ├── gui.py                    # Desktop interface
│   ├── ciphers.py                # Authenticated cipher implementations
│   ├── container.py              # Encrypted file format
│   ├── engine.py                 # Encryption/decryption workflows
│   ├── keys.py                   # Key derivation and key management
│   ├── batch.py                  # Batch processing
│   ├── audit.py                  # Tamper-evident audit log
│   ├── errors.py                 # Domain-specific errors
│   ├── settings.py               # Application settings
│   └── utils.py                  # Shared utilities
├── tests/
│   └── test_securecrypt.py       # Automated tests
├── docs/
│   └── screenshots/              # UI screenshots
├── run_cli.py                    # CLI launcher
├── run_gui.pyw                   # GUI launcher
├── requirements.txt              # Runtime dependencies
├── pyproject.toml                # Package/build configuration
└── README.md
```

## Requirements

- Python 3.9 or newer
- pip
- Tkinter for the desktop GUI (availability depends on your Python installation)

## Setup

Run these commands from this project directory.

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For editable installation and the `securecrypt` command, use:

```bash
pip install -e .
```

## Run the Application

**Interactive CLI**
```bash
python run_cli.py
```

**GUI**
```bash
python run_gui.pyw
```

If installed as a package, the CLI entry point is:

```bash
securecrypt
```

## Run Tests

Install the optional test dependencies, then run:

```bash
pip install -e ".[test]"
pytest -q
```

## Security Design Notes

1. **Authenticated encryption is essential.** Encryption alone does not guarantee integrity; authenticated cipher modes also validate ciphertext and associated data.
2. **Random keys and nonces matter.** SecureCrypt uses operating-system randomness for key material. Nonce uniqueness requirements remain critical for AEAD algorithms.
3. **Password strength is not a substitute for key derivation.** Argon2id/PBKDF2 increase the cost of offline guessing, but weak passphrases remain vulnerable.
4. **Keyfiles must be protected.** Anyone who obtains the required keyfile and passphrase may be able to decrypt protected data.
5. **Audit logs are not a complete security boundary.** A local MAC-chained log can help detect modifications, but an attacker who can alter the application and its key material may defeat it.

## Responsible Use

Use this project only on files you own or are authorized to protect. Keep backups of important data and test recovery before relying on encryption for critical files. **Do not treat this academic project as a formally audited or production-certified cryptographic product.**

## Academic Project

- **Project folder:** `2601240007_CTP_Project`
- **Course:** M.Tech CTP
- **Language:** Python

