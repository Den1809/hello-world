# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def make_dir():
    for i in range(1,10):
        dir_name = 'dir_'+str(i)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(dir_name,'created')
        else:
            print(dir_name, 'already exists')

def remove_dir():
    for file in os.listdir():
        if 'dir_' in file and os.path.isdir(file):
            os.rmdir(file)
            print(file,'removed')

make_dir()
remove_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

for i in os.listdir():
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

file_name = str(sys.argv[0]).split('/')[-1]
new_file_name =  'copy_'+file_name

shutil.copy(file_name,new_file_name)

