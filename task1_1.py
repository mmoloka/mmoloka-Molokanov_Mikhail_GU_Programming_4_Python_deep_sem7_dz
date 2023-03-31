from random import randint

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def get_file(extension: str, min_len_name: int=6, max_len_name: int=30, 
             min_count_bytes: int=256, max_count_bytes: int=4096, count_files: int=42) -> None:
    for _ in range(count_files):
            file_name = ''
            file_name_len = randint(min_len_name, max_len_name)
            for _ in range(file_name_len):
                file_name += chr(randint(ord('a'), ord('z')))
            random_byte = randint(min_count_bytes, max_count_bytes)
            data = bytes(random_byte)
            with open(f'{file_name}.{extension}', 'ab') as f:
                f.write(data)

def gen_files(extensions_dict: dict[str: int]) -> None:
     for extension in extensions_dict:
          get_file(extension, count_files=extensions_dict[extension])   

if __name__ == '__main__':
    gen_files({'txt': 3, 'doc': 2, 'pdf': 1})                       