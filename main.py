from asymmetric_cripto import AsymmetricEncryption
from symmetric_crypto import SymmetricalEncryption
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from work_with_files import read_binary_file, write_binary_file, read_json


def generate_keys(key_size, public_key_path: str,
                  private_key_path: str, encrypted_symmetric_key_path: str ) -> None:
    try:
        symmetric_key = SymmetricalEncryption.generate_key(key_size)
        private_key, public_key = AsymmetricEncryption.generate_rsa_keys()

        serialized_public = AsymmetricEncryption.serialization_asymmetric_public_key(public_key)
        serialized_private = AsymmetricEncryption.serialization_asymmetric_private_key(private_key)

        encrypted_symmetric_key = AsymmetricEncryption.rsa_encrypt(public_key, symmetric_key)

        write_binary_file(public_key_path, serialized_public)
        write_binary_file(private_key_path, serialized_private)
        write_binary_file(encrypted_symmetric_key_path, encrypted_symmetric_key)

    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе генерации ключей: {str(e)}")


def encrypt_data(original_text_path: str,
                 private_key_path: str,
                 encrypted_symmetric_key_path: str,
                 encrypt_text_path: str) -> None:
    try:
        original_text = read_binary_file(original_text_path)
        private_key_bytes = read_binary_file(private_key_path)
        encrypted_symmetric_key = read_binary_file(encrypted_symmetric_key_path)

        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )

        symmetric_key = AsymmetricEncryption.rsa_decrypt(private_key, encrypted_symmetric_key)

        encrypted_text = SymmetricalEncryption.encrypt_data(original_text, symmetric_key)
        write_binary_file(encrypt_text_path, encrypted_text)
    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе шифрования данных: {str(e)}")


def decrypt_data(encrypted_text_path: str,
                 private_key_path: str,
                 encrypted_symmetric_key_path: str,
                 decrypted_text_path: str) -> None:
    try:
        encrypted_text = read_binary_file(encrypted_text_path)
        private_key_bytes = read_binary_file(private_key_path)
        encrypted_symmetric_key = read_binary_file(encrypted_symmetric_key_path)

        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )

        symmetric_key = AsymmetricEncryption.rsa_decrypt(private_key, encrypted_symmetric_key)

        decrypted_text = SymmetricalEncryption.decrypt_data(encrypted_text, symmetric_key)
        write_binary_file(decrypted_text_path, decrypted_text)
    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе расшифровывания данных: {str(e)}")
