letter = "abcdefghijklmnopqrstuvwxyz"

symbol1 = input("Введите букву: ")
symbol2 = input("Введите букву: ")

print(f"{symbol1} стоит под номером {letter.index(symbol1) + 1}")
print(f"{symbol2} стоит под номером {letter.index(symbol2) + 1}")
print(f"Между ними {abs(letter.index(symbol1) - letter.index(symbol2)) - 1} символов")