import os

def view_dir():
    print('Содержимое папки',os.getcwd())
    for i in os.listdir():
        print('\t'+i)

def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Текущая папка успешно изменена на', dir_name)
    except:
        print('Ошибка перехода в папку', dir_name)

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
            print('Папка',dir_name,'успешно создана')
        except:
            print('Ошибка при создании папки',dir_name)

def remove_dir(dir_name):
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        try:
            os.rmdir(dir_name)
            print('Папка',dir_name,'удалена')
        except:
            print('Ошибка при удалении папки', dir_name)
    else: print('Папки', dir_name, 'не существует')
