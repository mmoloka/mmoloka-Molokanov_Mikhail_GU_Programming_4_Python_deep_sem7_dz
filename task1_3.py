import os

# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

def files_sort():
    os.mkdir('video')
    os.mkdir('music')
    os.mkdir('text')
    for obj in os.listdir():
        if os.path.isfile(obj) and obj.split('.')[1] in ['mp4', 'mov', 'avi']:
            os.replace(obj, os.path.join(os.getcwd(), 'video', obj))
        elif os.path.isfile(obj) and obj.split('.')[1] in ['mp3', 'wav', 'wma']:
            os.replace(obj, os.path.join(os.getcwd(), 'music', obj))
        elif os.path.isfile(obj) and obj.split('.')[1] in ['txt', 'doc', 'pdf']:
            os.replace(obj, os.path.join(os.getcwd(), 'text', obj))

if __name__ == '__main__':
    files_sort()