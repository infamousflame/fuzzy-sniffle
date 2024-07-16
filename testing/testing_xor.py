"""Testing the XOR encryption."""

from base64 import b64encode

from src.modules.encryption.cipher import XORCipher

key: bytes = b64encode(b'\xff\x00')
cipher: XORCipher = XORCipher(key)

ciphertext: bytes = cipher.encrypt(b'Hello, World!')
print(f'Ciphertext: {ciphertext}')

print(f'Plaintext: {cipher.decrypt(ciphertext)}')
