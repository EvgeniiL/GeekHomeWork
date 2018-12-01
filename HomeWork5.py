#EASY

import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

path = os.getcwd()
dirName = "/dir_"

for i in range(1, 10):
    os.mkdir(path + dirName + str(i))
print("Директории успешно созданы!")

del_choice = input("Хотите удалить созданные дирректории(y/...): ")

if del_choice == "y":
    for i in range(1, 10):
        os.rmdir(path + dirName + str(i))
    print("Директории успешно удалены!")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

path = os.getcwd()

files = os.listdir(path)
dirs = []

for file in files:
    if os.path.isdir(os.path.join(path, file)):
        dirs.append(file)

print(dirs)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def createCopyFile(path):
    if os.path.isfile(path):
        new_path = path + ".copy"
        shutil.copy(path, new_path)
        if os.path.exists(new_path):
            print("Файл успешно скопирован!")
        else:
            print("Файл не скопирован!")
    else:
        print("Вы не указали путь к ФАЙЛУ!")

choise = input("Вы хотите скопировать текущий файл(y/...): ")
if choise == "y":
    dir = os.getcwd()
    filePath = os.path.abspath(__file__)
    createCopyFile(filePath)

#NORMAL

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def menu():
    print("""
    1. Перейти в папку
    2. Просмотреть файлы указанной папки 
    3. Удалить папку
    4. Создать папку
    5. Выйти
    """)

def go_to_dir(path):
    if os.path.isdir(path):
        os.chdir(path)
        if os.getcwd() == path:
            print("Вы сменили директорию.")
        else:
            print("Произошла ошибка")
    else:
        print("Путь не указывет на папку!")

def create_dir(path):
    os.mkdir(path)
    if os.path.exists(path):
        print("Папка успешно создана!")
    else:
        print("Произошла ошибка")

def remove_dir(path):
    if os.path.isdir(path):
        os.rmdir(path)
        if not os.path.exists(path):
            print("Папка успешно удалена!")
        else:
            print("Произошла ошибка")
    else:
        print("Путь не указывет на папку!")

def see_files(path):
    if os.path.isdir(path):
        print(os.listdir(path))
    else:
        print("Путь не указывет на папку!")

user_answer = None

while True:
    menu()
    user_answer = input("Выберите пункт(1-5): ")
    if user_answer == "1":
        path = input("Введите путь к папке, в которую хотите перейти: ")
        go_to_dir(path)
    elif user_answer == "2":
        path = input("Введите путь к папке: ")
        see_files(path)
    elif user_answer == "3":
        path = input("Введите путь к папке, которую хотите удалить: ")
        remove_dir(path)
    elif user_answer == "4":
        path = input("Какой путь будет у новой папки?: ")
        create_dir(path)
    elif user_answer == "5":
        break
    else:
        print("что вы хотите?")

#HARD

def make_dirs(arrDirs, path):
    for exp in arrDirs:
        if not os.path.exists(os.path.join(path, exp)):
            os.mkdir(os.path.join(path, exp))

def remove_dirs(arrDirs, path):
    for dir in arrDirs:
        os.rmdir(os.path.join(path, dir))

print("Сортировка файлов")

choise = input("Хотите просортировать файлы?(y/...):")

if choise == "y":
    path = input("Введите путь к файлу: ")
    if os.path.isdir(path):
        files = os.listdir(path)
        if len(files) > 0:
            expansions = set([os.path.splitext(file)[-1] for file in files if os.path.isfile(os.path.join(path, file))])

            make_dirs(expansions, path)

            for file in files:
                if os.path.isfile(os.path.join(path, file)):
                    exp = os.path.splitext(os.path.join(path, file))[-1]
                    os.rename(os.path.join(path, file), os.path.join(path, exp, file))
            print("Файлы просортированны")
        else:
            print("Сортировать нечегo:)")
    else:
        print("Данный путь не указывает на папку!")

print("Рассортировка файлов")

choise = input("Хотите рассортировать файлы?(y/...):")

if choise == "y":
    path = input("Введите путь к файлу: ")
    if os.path.isdir(path):
        files = os.listdir(path)
        dirs = [file for file in files if os.path.isdir(os.path.join(path, file))]
        if len(dirs) > 0:
            for dir in dirs:
                for file in os.listdir(os.path.join(path, dir)):
                    os.rename(os.path.join(path, dir, file), os.path.join(path, file))
            remove_dirs(dirs, path)
            print("Файлы рассортированны")
        else:
            print("Файлы уже рассортированны:)")
    else:
        print("Такой папки нет на вашем компьютере")

