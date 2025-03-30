import json


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        raise FileNotFoundError(f"File not found")


def read_json(file_name: str) -> dict:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        raise FileNotFoundError(f"File not found")


def write_file(file_name: str, text: str) -> None:
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        raise IOError(f"Couldn't write to a file")

def сaesar_cipher(plain_text, key, alphabet):
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
        constants = read_json('task1/consts.json')
        key = read_json('task1/key.json')
        plain_text = read_file('task1/plain_text.txt')

        encrypted_text = сaesar_cipher(plain_text, key['key'], constants['alphabet'])
        write_file('task1/encrypted_text.txt', encrypted_text)

        print('The encrypted text is in the encrypted_text.txt')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
