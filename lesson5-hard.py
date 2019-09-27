# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <object_name> - создание директории")
    print("cp - <file_name> <new_file_name> - копирование файла")
    print("rm - <file_name> - удаление файла")
    print("cd - <path> - смена директории")
    print("ls - содержимое директории")

def make_dir():
    if not object_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), object_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(object_name))
    except FileExistsError:
        print('директория {} уже существует'.format(object_name))

def ping():
    print("pong")

def copy_file():
    if object2_name == None:
        exit()
    try:
        shutil.copy(object_name, object2_name)
        print('Файл', object_name, 'скопирован в файл', object2_name)
    except:
        print('Ошибка копирования файла',object_name)

def delete_file():
    if os.path.exists(object_name):
        print('Удаление файла',object_name)
        if input('Удалить файл? ').upper() == 'Y':
            try:
                os.remove(object_name)
                print('Файл', object_name, 'удален')
            except:
                print('Ошибка удаления файла',object_name)
    else:
        print('Файла с именем',object_name,'не существует')

def view_dir():
    print('Содержимое папки',os.getcwd()+'\n')
    for i in os.listdir():
        print(''+i)

def change_dir():
    try:
        os.chdir(object_name)
        print('Текущая папка успешно изменена на', object_name)
    except:
        print('Ошибка перехода в папку', object_name)
    view_dir()

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": view_dir,
    "cp": copy_file,
    "rm": delete_file,
    "cd": change_dir
}

try:
    object_name = sys.argv[2]
except IndexError:
    object_name = None

try:
    object2_name = sys.argv[3]
except IndexError:
    object2_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")