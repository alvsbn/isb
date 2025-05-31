import json


def read_json(file_name: str) -> dict:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден")
    except IOError:
        raise IOError(f"Ошибка чтения файла")
    except Exception as e:
        raise Exception(f"Ошибка: {str(e)}")


def read_binary_file(file_name: str) -> bytes:
    try:
        with open(file_name, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден")
    except IOError:
        raise IOError(f"Ошибка чтения файла")
    except Exception as e:
        raise Exception(f"Ошибка: {str(e)}")


def write_binary_file(file_name: str, text: bytes) -> None:
     try:
        with open(file_name, 'wb') as file:
             file.write(text)
     except IOError:
        raise IOError(f"Ошибка записи в файл")
     except Exception as e:
         raise Exception(f"Ошибка: {str(e)}")