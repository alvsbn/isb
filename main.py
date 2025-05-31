from asymmetric_cripto import AsymmetricEncryption
from symmetric_crypto import SymmetricalEncryption
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from work_with_files import read_binary_file, write_binary_file, read_json
import argparse


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
        raise RuntimeError(f"Ошибка в процессе дешифрования данных: {str(e)}")


def main() -> None:
    try:
        parser = argparse.ArgumentParser()

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-gen', '--generation', action='store_true', help='Режим генерации ключей')
        group.add_argument('-enc', '--encryption', action='store_true', help='Режим шифрования')
        group.add_argument('-dec', '--decryption', action='store_true', help='Режим дешифрования')

        args = parser.parse_args()

        settings = read_json('settings.json')

        match (args.generation, args.encryption, args.decryption):
            case (True, False, False):
                print("Запущен режим генерации ключей")
                generate_keys(
                    settings['key_size'],
                    settings['public_key'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key']
                )
                print("Генерация ключей завершена")

            case (False, True, False):
                print("Запущен режим шифрования")
                encrypt_data(
                    settings['original_text'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key'],
                    settings['encrypted_text']
                )
                print("Шифрование завершено")

            case (False, False, True):
                print("Запущен режим дешифрования")
                decrypt_data(
                    settings['encrypted_text'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key'],
                    settings['decrypted_text']
                )
                print("Дешифрование завершено")
            case _:
                raise ValueError("Не выбран режим работы")

    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == '__main__':
    main()