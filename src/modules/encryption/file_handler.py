"""Handles the encryption and decryption of files."""

from src.modules.encryption.cipher import Cipher


def encrypt_file(
        file_path: str, cipher: Cipher, out: str | None = None
        ) -> None:
    """Encrypts the given file using the specified cipher."""
    if out is None:
        out = file_path + '.enc'
    with (
        open(file_path, 'rb') as plaintext,
        open(out, 'wb') as ciphertext
    ):
        ciphertext.write(cipher.encrypt(plaintext.read()))


def decrypt_file(
        file_path: str, cipher: Cipher, out: str | None = None
        ) -> None:
    """Decrypts the given file using the specified cipher."""
    if out is None:
        if file_path.endswith('.enc'):
            out = file_path[:-4]
        else:
            out = file_path + '.dec'
    with (
        open(file_path, 'rb') as ciphertext,
        open(out, 'wb') as plaintext
    ):
        plaintext.write(cipher.decrypt(ciphertext.read()))
