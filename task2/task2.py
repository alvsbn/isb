from work_with_files import read_json, read_file, write_file, write_json


def frequency_analysis(text: str) -> dict:
    """
    Performs frequency analysis of symbols
    :param text: text
    :return: dictionary
    """
    text = text.replace("\n", "")
    total_chars = len(text)
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        freq[char] = freq[char] / total_chars

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_freq)


def key_dict(freq1: dict, freq2: dict) -> dict:
    """
    Creates a dictionary of comparisons between two frequency distributions
    :param freq1: the first frequency distribution
    :param freq2: the second frequency distribution
    :return: dictionary with keys
    """
    new_dict = {}
    keys1 = list(freq1.keys())
    keys2 = list(freq2.keys())

    min_len = min(len(keys1), len(keys2))

    for i in range(min_len):
        new_dict[keys2[i]] = keys1[i]

    return new_dict


def decrypt_text(encrypted_text: str, key_dict: dict) -> str:
    """
    Decrypts text using a dictionary with keys
    :param encrypted_text: encrypted text
    :param key_dict: dictionary with keys
    :return: decrypt text
    """
    decrypted_text = ""

    for char in encrypted_text:
        if char in key_dict:
            decrypted_text += key_dict[char]
        else:
            decrypted_text += char

    return decrypted_text


def main():
    try:
        constants = read_json('consts.json')

        encrypted_text = read_file(constants['cod1'])
        new_freq = frequency_analysis(encrypted_text)
        write_json(constants['freq_cod1'], new_freq)
        freq1 = read_json(constants['frequencies'])
        freq2 = read_json(constants['freq_cod1'])
        keys = key_dict(freq1, freq2)
        write_json(constants['keys'], keys)
        decrypted_text = decrypt_text(encrypted_text, keys)
        write_file(constants['decrypted_text'], decrypted_text)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()