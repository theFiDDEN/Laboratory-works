import math


def task1(degree):
    print('Задание 1')
    print(degree, '° = ', degree / 180, 'π', sep='')


def task2(radian):
    print('Задание 2')
    print(radian, 'π = ', radian * 180, '°', sep='')


def task3(A, X, Y):
    print('Задание 3')
    print('Цена ', X, ' килограмм конфет стоит ', A, ' рублей', sep='')
    print(Y, ' килограмм конфет стоит ', Y / X * A, ' рублей', sep='')


def task4(v1, v2, t):
    print('Задание 4')
    print('Скорость 1 автомобиля: ', v1, ' км\ч', sep='')
    print('Скорость 2 автомобиля: ', v2, ' км\ч', sep='')
    print('Через ', t, ' ч они удалятся друг от друга на ', abs(v1 - v2) * t, ' км', sep='')


def task5(A, B):
    print('Задание 5')
    if A == 0:
        print('Некорректно введенные данные: коэффициент A равен 0')
        return 0
    print('Уравнение ', A, ' * x + ', B, ' = 0 при x = ', -B / A, sep='')


def task6(a1, b1, c1, a2, b2, c2):
    print('Задание 6')
    d = a1 * b2 - a2 * b1
    dx = c1 * b2 - c2 * b1
    dy = a1 * c2 - a2 * c1

    x = dx / d
    y = dy / d

    print('Решение для системы уравнений')
    print(a1, ' * x + ', b1, ' * y = ', c1, sep='')
    print(a2, ' * x + ', b2, ' * y = ', c2, sep='')
    print('(X, Y) : (', x, ', ', y, ')', sep='')


task1(60)
print('')

task2(1 / 3)
print('')

task3(6, 2, 3)
print('')

task4(4, 7, 3)
print('')

task5(2, 3)
print('')

task6(6, 7, 2, 5, 8, 3)
print('')
