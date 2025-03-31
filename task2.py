import json
from task1 import read_json, read_file, write_file


def write_json(file_name: str, text: dict) -> None:
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(text, file, ensure_ascii=False, indent=4)
    except:
        raise IOError(f"Couldn't write to a file")


def frequency_analysis(file_name: str) -> dict:
    file_name = file_name.replace("\n", "")
    total_chars = len(file_name)
    freq = {}

    for char in file_name:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        freq[char] = freq[char] / total_chars

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_freq)

def key_dict(freq1: dict, freq2: dict) -> dict:
    new_dict = {}
    keys1 = list(freq1.keys())
    keys2 = list(freq2.keys())

    min_len = min(len(keys1), len(keys2))

    for i in range(min_len):
        new_dict[keys2[i]] = keys1[i]

    return new_dict


def decrypt_text(encrypted_text: str, key_dict: dict) -> str:
     decrypted_text = ""

     for char in encrypted_text:
         if char in key_dict:
            decrypted_text += key_dict[char]
         else:
            decrypted_text += char

     return decrypted_text


def main():
    try:
        encrypted_text = read_file('task2/cod1.txt')
        new_freq = frequency_analysis(encrypted_text)
        write_json('task2/freq_cod1.json', new_freq)
        freaq1 = read_json('task2/frequencies.json')
        freaq2 = read_json('task2/freq_cod1.json')
        keys = key_dict(freaq1, freaq2)
        write_json('task2/keys.json', keys)
        decrypted_text = decrypt_text(encrypted_text, keys)
        write_file('task2/decrypted.txt', decrypted_text)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()