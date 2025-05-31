from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

class SymmetricalEncryption:

    @staticmethod
    def generate_key(key_size: int) -> bytes:
        if key_size not in [128, 192, 256]:
            raise ValueError("Размер ключа не подходит")

        return os.urandom(key_size // 8)

    @staticmethod
    def padding_data(data: bytes) -> bytes:
        padder = padding.ANSIX923(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    @staticmethod
    def encrypt_data(data: bytes, key: bytes) -> bytes:
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(SymmetricalEncryption.padding_data(data)) + encryptor.finalize()

        return iv + ciphertext

    @staticmethod
    def unpadding_data(data: bytes) -> bytes:
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_data = unpadder.update(data) + unpadder.finalize()
        return unpadded_data

    @staticmethod
    def decrypt_data(data: bytes, key: bytes) -> bytes:
        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        return SymmetricalEncryption.unpadding_data(padded_data)