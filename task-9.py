a = float(input("Введите первое число: "))
b = float(input("Введите  второе число: "))
c = float(input("Введите  третье число: "))

if a > b > c or a < b < c:
    print(f"среднее числс: {b}")
elif b < a < c or b > a > c:
    print(f"среднее числс: {a}")
else:
    print(f"среднее числс: {c}")
