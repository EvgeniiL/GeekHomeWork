"""
Normal

Задача-1:
Дан список, заполненный произвольными целыми числами, получите новый список,
элементами которого будут квадратные корни элементов исходного списка,
но только если результаты извлечения корня не имеют десятичной части и
если такой корень вообще можно извлечь
Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
"""

arr = [2, -5, 8, 9, -25, 25, 4]
arr_new = []

for i in arr:
    if i >= 0 and i**0.5 % 1 == 0:
        arr_new.append(int(i**0.5))
print(arr_new)

"""
Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
Склонением пренебречь (2000 года, 2010 года)
"""

date = "03.08.2001"

days = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
    '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
    '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
    '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
    '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
}

mounths = {
    "01" : "января", "02" : "февраля", "03" : "марта", "04" : "апреля",
    "05" : "мая", "06" : "июня", "07" : "июля", "08" : "августа",
    "09" : "сентября", "10" : "октября", "11" : "ноября", "12" : "декабря"
}

date = [i for i in date.split(".")]

print(f"{days[date[0]]} {mounths[date[1]]} {date[2]} года.")

"""
Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
в диапазоне от -100 до 100. В списке должно быть n - элементов.
Подсказка:
для получения случайного числа используйте функцию randint() модуля random
"""
import random

n = int(input("Введите кол-во элементов в списке: "))
arr = []

for i in range(n):
    arr.append(random.randint(-100, 100))
print(arr)

"""
Задача-4: Дан список, заполненный произвольными целыми числами.
Получите новый список, элементами которого будут:
а) неповторяющиеся элементы исходного списка:
например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
б) элементы исходного списка, которые не имеют повторений:
например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
"""

arr = [1, 2, 4, 5, 6, 2, 5, 2, 5, 2, 8, 9, 9]
print(list(set(arr)))

for i in arr:
    if arr.count(i) > 1:
        while arr.count(i) != 0:
            arr.remove(i)

print(arr)
