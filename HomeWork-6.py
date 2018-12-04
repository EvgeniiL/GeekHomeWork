import random
#EASY-NORMAL

# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.c + self.b <= self.a:
            print("Такого треуголника нет!")
            exit(1)

    def square(self):
        self.p = (self.a + self.b + self.c) / 2
        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def draw(self):
        print(f"({self.a}, {self.b}, {self.c})")

#HARD

# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка

# Чем логичнее код тем лучше

class matr():
    def __init__(self, height, width, symbol):
        self.height = height
        self.width = width
        self.symbol = symbol

    def draw(self):
        self.matr = [[str(self.symbol) for i in range(self.width)] for i in range(self.height)]
        for i in self.matr:
            print(" ".join(i))

    def random_symbols(self):
        self.matr = [["0" for i in range(self.width)] for i in range(self.height)]
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                self.matr[i][j] = str(random.randrange(0, 11))
            print(" ".join(self.matr[i]))

    def height_width(self):
        print(f"width: {self.width}; height: {self.height}")

    def len_matr(self):
        print(f"{self.width * self.height} elements")

