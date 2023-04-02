from pathlib import Path

# Напишите функцию группового переименования файлов. Она должна:
# ✔  принимать параметр желаемое конечное имя файлов.
#     При переименовании в конце имени добавляется порядковый номер.
# ✔  принимать параметр количество цифр в порядковом номере.
# ✔  принимать параметр расширение исходного файла.
#     Переименование должно работать только для этих файлов внутри каталога.
# ✔  принимать параметр расширение конечного файла.
# ✔  принимать диапазон сохраняемого оригинального имени. Например для диапазона
#    [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
#    желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

def rename_files(count_digits: int, original_extension: str, final_extension: str,
                 range_original_name: list[int], final_name: str = '') -> None:
    number = 0
    number_str = ''
    for obj in Path(Path().cwd()).iterdir():
        if obj.is_file() and str(obj).split('.')[1] == original_extension:
            obj_list = str(obj).split('\\')
            original_name = obj_list[len(obj_list) - 1]
            cut_original = original_name.split('.')[0][range_original_name[0] - 1:range_original_name[1]]
            number += 1
            if count_digits <= len(str(number)):
                number_str = str(number)
            elif count_digits > len(str(number)):
                number_str = '0'* (count_digits - len(str(number))) + str(number)   
            Path(original_name).rename(f'{cut_original}{final_name}{number_str}.{final_extension}')

if __name__ == '__main__':
    rename_files(3, 'txt', 'doc', [4, 5], 'document')
