import math

def square(side):
    side_0 = math.ceil(side)
    return side_0 ** 2

side_1 = float(input('Введите сторону квадрата: '))
print(f'Площадь квадрата равна {square(side_1)}')
