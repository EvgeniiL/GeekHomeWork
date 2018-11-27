#EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

arr = [1, 2, 4, 0]

arr_new = [i**2 for i in arr]
print(arr_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["банан", "яблоко", "апельсин", "ананас", "груша"]
fruits2 = ["гранат", "банан", "апельсин", "мандарин"]

fruits = [fruit for fruit in fruits1 if fruit in fruits2]
print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

arr = [2, 5, -2, -24, 3, 12, 15]

arr_new = [i for i in arr if i % 3 == 0 and i % 4 != 0 and i > 0]
print(arr_new)

#NORMAL

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер

import random
size = int(input("Введите размер матрицы: "))

matr = [[random.randrange(1,10) for j in range(size)] for i in range(size)]

for row in range(len(matr)):
    matr[row][random.randrange(len(matr))] = 0
    print(" ".join([str(i) for i in matr[row]]))

#HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений? 
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

import requests

r = requests.get("https://uploads.hb.cldmail.ru/asset/1198400/attachment/bef1297ba636c1d663d2f7ae4087efd5.txt")

passwords = [[str(i) for i in log.split(";")][1] for log in r.text.split("\n") if log != "\r" and log != ""]

noRepeatPassword = list(set(passwords))

countPassword = []

for i in noRepeatPassword:
    countPassword.append(passwords.count(i))

d = dict(zip(passwords, countPassword))
d = sorted(d.items(), key=lambda x: x[1])

top_passords = []
top_counts = []

for i in range(len(d) - 1, len(d) - 11, -1):
    new_str = d[i][0].replace("\r", "")
    top_passords.append(new_str)
    top_counts.append(d[i][1])

top = dict(zip(top_passords, top_counts))

for index, password in enumerate(top, start = 1):
    print(f"{index}. {password}")

#
#
# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3 
# 8 9 4
# 7 6 5
