import math


def square(side):
    area = side ** 2
    if not isinstance(side, int):
        return math.ceil(area)
    return area


side = 6.7
result = square(side)
print(f"Сторона кадрата: {side} Площадь: {result}")
