"""Makes some testing files to encrypt."""

from src.modules.encryption.cipher import XORCipher
from src.modules.encryption.file_handler import decrypt_file, encrypt_file

FILE_TEXT = """This is a testing file.
If this file does not say 'Hello World!', then something went terribly wrong.
Hello, World!
"""

with open('test_file.txt', 'w') as file:
    file.write(FILE_TEXT)

cipher: XORCipher = XORCipher('SGVsbG8sIHdvcmxkIQ==')

encrypt_file('test_file.txt', cipher, 'ciphertext.dat')
decrypt_file('ciphertext.dat', cipher)

encrypt_file('test_file.txt', cipher)
decrypt_file('test_file.txt.enc', cipher)
