"""
Hard

Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
1. Сколько слов в тексте?
2. Сколько букв английского алфавита в тексте?
"""

Eng = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f",
    "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"
]

text = input("Введите текст: ").lower()
text = [i for i in text.split(" ")]

Eng_words = 0

for i in text:
    for j in i:
        if j in Eng:
            Eng_words += 1
print(len(text))
print(Eng_words)


"""
Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
"""

text1 = input("Введите первый текст: ").lower()
text1 = [i for i in text1.split(" ")]

text2 = input("Введите второй текст: ").lower()
text2 = [i for i in text2.split(" ")]

repeat_words = []

for i in text1:
    if i in text2:
        repeat_words.append(i)

if len(repeat_words) != 0:
    print(repeat_words)
else:
    print("Повторяющихся слов нет!")