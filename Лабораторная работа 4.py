import math


def task1(a, b):
    print('Сторона A =', a)
    print('Сторона B =', b)
    print('Площадь прямоугольника =', a * b)
    print('Периметр прямоугольника =', 2 * (a + b))


def task2(d):
    print('Диаметр окружности =', d)
    print('Длина окружности =', 3.14 * d)


def task3(a, b):
    print('Число a =', a)
    print('Число b =', b)
    print('Среднее арифметическое =', (a + b) / 2)


def task4(a, b):
    print('Число a =', a)
    print('Число b =', b)
    print('Сумма квадратов чисел =', a ** 2 + b ** 2)
    print('Разность квадратов чисел =', a ** 2 - b ** 2)
    print('Произведение квадратов чисел =', a ** 2 * b ** 2)
    print('Частное квадратов чисел =', a ** 2 / b ** 2)


def task5(a, b):
    print('Число a =', a)
    print('Число b =', b)
    print('Сумма модулей чисел =', abs(a) + abs(b))
    print('Разность модулей чисел =', abs(a) - abs(b))
    print('Произведение модулей чисел =', abs(a) * abs(b))
    print('Частное модулей чисел =', abs(a) / abs(b))


task1(3, 5)
print('\n')

task2(3)
print('\n')

task3(3, 5)
print('\n')

task4(3, 5)
print('\n')

task5(3, 5)
