import random

letter = "abcdefghijklmnopqrstuvwxyz"

min_ = input("диапазон от: ")
max_ = input("до: ")

if min_ in letter and max_ in letter:
    print(f"Ваш символ: {letter[random.randint(letter.index(min_), letter.index(max_))]}")
else:
    print(f"Целое число: {int(random.randint(int(min_), int(max_)))}")
    print(f"Вещественное число: {float(random.randint(int(min_), int(max_)))}")