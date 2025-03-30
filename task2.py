import json
from task1 import read_json, read_file, write_file

def write_json(file_name: str, text: dict) -> None:
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(text, file, ensure_ascii=False, indent=4)
    except:
        raise IOError(f"Couldn't write to a file")

def frequency_analysis(file_name: str) -> dict:
    total_chars = len(file_name)
    freq = {}
    file_name = file_name.replace("\n", "")

    for char in file_name:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        freq[char] = freq[char] / total_chars

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_freq)


def main():
    try:
        encrypted_text = read_file('task2/cod1.txt')
        new_freq = frequency_analysis(encrypted_text)
        write_json('task2/freq_cod1.json', new_freq)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()