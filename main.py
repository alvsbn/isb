from asymmetric_cripto import AsymmetricEncryption
from symmetric_crypto import SymmetricalEncryption
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


