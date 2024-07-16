"""Handles the encryption and decryption of files."""

from src.modules.encryption.cipher import Cipher


def encrypt_file(
        file_path: str, cipher: Cipher, out: str | None = None
        ) -> None:
    """
    Encrypts the file at the specified file path using the provided cipher and
    writes the encrypted content to a new file.

    Args:
        file_path (str): The path to the file to be encrypted.
        cipher (Cipher): The cipher object used for encryption.
        out (str | None, optional): The path to store the encrypted file. If
            None, a default path with '.enc' extension is used. Defaults to
            None.

    Returns:
        None
    """
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
    """
    Decrypts the file at the specified file path using the provided cipher and
    writes the decrypted content to a new file.

    Args:
        file_path (str): The path to the file to be decrypted.
        cipher (Cipher): The cipher object used for decryption.
        out (str | None, optional): The path to store the decrypted file. If
            None, a default path with '.dec' extension is used. Defaults to
            None.

    Returns:
        None
    """
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
