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

    if not A < B < C:
        print('Точка C не расположена между точками A и B')
        return 0

    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Произведение длин отрезков AC и BC =', abs(A - C) * abs(B - C))


def task4(x1, y1, x2, y2):
    print('Координаты точек (', x1, ',', y1, ')', 'и', '(', x2, ',', y2, ')')
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    print('Периметр прямоугольника =', 2 * (a + b))
    print('Площадь прямоугольника =', a * b)


def task5(x1, y1, x2, y2, x3, y3):
    print('Координаты треугольника: (', x1, ',', y1, '),', '(', x2, ',', y2, '),', '(', x3, ',', y3, ')')
    A = [x1, y1]
    B = [x2, y2]
    C = [x3, y3]
    H = [abs(x1 - x3) / 2, abs(y1 - y3) / 2]

    AC = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    AB = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    BC = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    BH = ((B[0] - H[0]) ** 2 + (B[1] - H[1]) ** 2) ** 0.5

    print('Площадь треугольника =', AC * BH / 2)
    print('Периметр треугольника =', AB + AC + BC)


task1(1, 2, 3, 4)
print()

task2(1, 2, 3)
print()

task3(1, 2, 3)
print()

task4(1, 2, 3, 4)
print()

task5(0, 0, 2, 4, 6, 1)
