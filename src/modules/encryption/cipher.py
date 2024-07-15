"""Uses the cryptography library to encrypt and decrypt data."""

from abc import ABC, abstractmethod


class Cipher(ABC):
    """A Cipher used for encryption and decryption."""

    CIPHER = None

    def __init__(self, key: bytes) -> None:
        """
        Initializes the object with the given key.

        Args:
            key (bytes): The key used for encryption and decryption.

        Returns:
            None
        """
        self.key = key
        self.key_length = len(key)

    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypts the given data using the specified encryption algorithm.

        Args:
            data (bytes): The data to be encrypted.

        Returns:
            bytes: The encrypted data.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes:
        """
        Decrypts the given data using the specified encryption algorithm.

        Args:
            data (bytes): The data to be decrypted.

        Returns:
            bytes: The decrypted data.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass


class XORCipher(Cipher):
    """A Cipher used for encryption and decryption.

    This uses a simple XOR encryption for now.
    """

    CIPHER = 'XOR'

    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypts the given data using XOR encryption.

        Args:
            data (bytes): The data to be encrypted.

        Returns:
            bytes: The encrypted data.
        """
        return bytes([
            byte ^ self.key[i % self.key_length]
            for i, byte in enumerate(data)
        ])

    def decrypt(self, data: bytes) -> bytes:
        """
        Decrypts the given data using the same encryption algorithm as the 
        encrypt method.

        Args:
            data (bytes): The data to be decrypted.

        Returns:
            bytes: The decrypted data.
        """
        return self.encrypt(data)
