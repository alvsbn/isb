from work_with_files import read_json, read_file, write_file


def caesar_cipher(plain_text: str, key: str, alphabet: str) -> str:
    """
    Encrypts a text using Caesar cipher algorithm
    :param plain_text: plain text
    :param key: key
    :param alphabet: alphabet
    :return: encrypted text
    """
    text = plain_text.lower()
    key_length = len(key)
    encrypted_text = ''

    for letter in text:
        position = alphabet.find(letter)
        new_position = (position + key_length) % len(alphabet)
        if letter in alphabet:
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    return encrypted_text


def caesar_decrypt(encrypted_text: str, key: str, alphabet: str) -> str:
    """
    Decrypts a text using Caesar cipher algorithm
    :param encrypted_text: encrypted text
    :param key: key
    :param alphabet: alphabet
    :return: decrypted text
    """
    text = encrypted_text.lower()
    key_length = len(key)
    decrypted_text = ''

    for letter in text:
        position = alphabet.find(letter)
        new_position = (position - key_length) % len(alphabet)
        if letter in alphabet:
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    return decrypted_text


def main():
    try:
        constants = read_json('consts.json')

        key = read_json(constants['key'])
        plain_text = read_file(constants['plain_text'])

        encrypted_text = caesar_cipher(plain_text, key['key'], constants['alphabet'])
        write_file(constants['encrypted_text'], encrypted_text)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
