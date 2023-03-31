import os
from task1_1 import*

# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def file_to_dir(extensions_dict: dict[str: int], dir: str) -> None:
    existance = False
    for obj in os.listdir():
        if obj == dir and os.path.isdir(obj):
            existance = True
    if not existance:
        os.mkdir(dir)        
    gen_files(extensions_dict)
    for obj in os.listdir():
        if os.path.isfile(obj) and (obj.split('.')[1] in extensions_dict.keys()):
            if obj not in os.listdir(dir):
                os.replace(obj, os.path.join(os.getcwd(), dir, obj))
            else:
                os.replace(obj, os.path.join(os.getcwd(), dir, obj.split('.')[0] + '_.' + obj.split('.')[1]))   

if __name__ == '__main__':
    file_to_dir({'txt': 3, 'doc': 2, 'pdf': 1}, 'directory')


