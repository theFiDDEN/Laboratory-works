import math


def task1():
    print('\n')
    print('Задание 1')

    x1 = int(input('Введите координату x1: '))
    y1 = int(input('Введите координату y1: '))
    x2 = int(input('Введите координату x2: '))
    y2 = int(input('Введите координату y2: '))

    print('Расстояние между ними =', ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    print('\n')


def task2():
    print('\n')
    print('Задание 2')

    A = int(input('Введите координату A: '))
    B = int(input('Введите координату B: '))
    C = int(input('Введите координату C: '))

    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Сумма длин отрезков AC и BC =', abs(A - C) + abs(B - C))
    print('\n')


def task3():
    print('\n')
    print('Задание 3')

    A = int(input('Введите координату A: '))
    B = int(input('Введите координату B: '))
    C = int(input('Введите координату C: '))

    if not A < B < C:
        print('Точка C не расположена между точками A и B')
        return 0

    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Произведение длин отрезков AC и BC =', abs(A - C) * abs(B - C))
    print('\n')


def task4():
    print('\n')
    print('Задание 4')

    x1 = int(input('Введите координату x1: '))
    y1 = int(input('Введите координату y1: '))
    x2 = int(input('Введите координату x2: '))
    y2 = int(input('Введите координату y2: '))

    a = abs(x2 - x1)
    b = abs(y2 - y1)

    print('Периметр прямоугольника =', 2 * (a + b))
    print('Площадь прямоугольника =', a * b)
    print('\n')


def task5():
    print('\n')
    print('Задание 5')

    x1 = int(input('Введите координату x1: '))
    y1 = int(input('Введите координату y1: '))
    x2 = int(input('Введите координату x2: '))
    y2 = int(input('Введите координату y2: '))
    x3 = int(input('Введите координату x3: '))
    y3 = int(input('Введите координату y3: '))

    a = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    b = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5

    P = a + b + c  # Периметр
    s = P / 2  # Полупериметр

    print('Площадь треугольника =', ((s * (s - a) * (s - b) * (s - c)) ** 0.5))
    print('Периметр треугольника =', P)
    print('\n')


tasks = [task1, task2, task3, task4, task5]
while True:
    tasks[int(input('Перейти к заданию: ')) - 1]()
