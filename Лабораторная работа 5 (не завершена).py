import math


def task1(x1, y1, x2, y2):
    print('Координаты точек (', x1, ',', y1, ')', 'и', '(', x2, ',', y2, ')')
    print('Расстояние между ними =', ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

def task2(A, B, C):
    print('Точка A =', A)
    print('Точка B =', B)
    print('Точка C =', C)
    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Сумма длин отрезков AC и BC =', abs(A - C) + abs(B - C))

def task3(A, B, C):
    print('Точка A =', A)
    print('Точка B =', B)
    print('Точка C =', C)
    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Произведение длин отрезков AC и BC =', abs(A - C) * abs(B - C))