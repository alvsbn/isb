import json


def read_file(file_name: str) -> str:
    """
    Reads the contents of the file
    :param file_name: file name
    :return: file contents
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        raise FileNotFoundError(f"File not found")


def read_json(file_name: str) -> dict:
    """
    Reads the contents of a json file
    :param file_name: file name
    :return: dictionary
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        raise FileNotFoundError(f"File not found")


def write_file(file_name: str, text: str) -> None:
    """
    Writes the content to a file
    :param file_name: file name
    :param text: file contents
    :return: None
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        raise IOError(f"Couldn't write to a file")


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
