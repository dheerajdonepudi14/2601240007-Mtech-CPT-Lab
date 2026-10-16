"""Launcher for the SecureCrypt desktop GUI."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from securecrypt.gui import main  # noqa: E402

main()
