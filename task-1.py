x = int(input("введите трехзначное целое число x: "))
summ = 0
mult = 1
n = 0

n = x % 10
summ += n
mult *= n

x //= 10
n = x % 10
summ += n
mult *= n

x //= 10
n = x % 10
summ += n
mult *= n

print(f"Сумма чисел: {summ}\nПроизведение чисел: {mult}")