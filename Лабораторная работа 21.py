import math
import random


def is_unique(arr):
    for x in arr:
        if arr.count(x) != 1:
            return 0
    return 1


def fill_matrix(M, N):
    arr = []

    while not arr or not is_unique([a for b in arr for a in b]):
        arr.clear()
        for x in range(M):
            arr.append([])
            for y in range(N):
                arr[-1].append(random.randint(0, 100))

    return arr


def average(arr):
    result = 0
    for x in arr:
        result += x
    return result / len(arr)


def only_odds(arr):
    for x in arr:
        if not x % 2:
            return False
    return True


def task1():
    print('Задание 1')

    M = int(input('Введите порядок матрицы (нечетное число): '))
    arr = fill_matrix(M, M)

    print('Матрица:')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    print('Вывести все элементы против часовой стрелки:')
    for temp in range(len(arr) // 2):
        for x in range(temp, len(arr) - temp):
            print(arr[x][temp], end=' ')
        for y in range(temp + 1, len(arr) - temp):
            print(arr[len(arr) - 1 - temp][y], end=' ')

        for x in range(len(arr) - 1 - temp - 1, temp - 1, -1):
            print(arr[x][len(arr) - 1 - temp], end=' ')
        for y in range(len(arr) - 1 - temp - 1, temp, -1):
            print(arr[temp][y], end=' ')

    print(arr[len(arr) // 2][len(arr) // 2])


def task2():
    print('Задание 2')

    M = int(input('Введите количество строк матрицы: '))
    N = int(input('Введите количество столбцов матрицы: '))
    K = int(input('Введите целое число K: '))
    arr = fill_matrix(M, N)

    print('Матрица:')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    multiplication = 1
    amount = 0
    for x in arr[K - 1]:
        multiplication *= x
        amount += x

    print('')
    print('Сумма элементов К-й строки:', amount)
    print('Произведение элементов К-й строки:', multiplication)


def task3():
    print('Задание 3')

    M = int(input('Введите количество строк матрицы: '))
    N = int(input('Введите количество столбцов матрицы: '))
    arr = fill_matrix(M, N)

    print('Матрица:')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    index = 0
    min = 999999
    for y in range(N):
        multiplication = 1
        for x in range(M):
            multiplication *= arr[x][y]
        if multiplication < min:
            min = multiplication
            index = y

    print('\n', 'Номер столбца с наименьшим произведением элементов: ', index + 1, sep='')
    print('Значение наименьшего произведения:', min)


def task4():
    print('Задание 4')

    M = int(input('Введите количество строк матрицы: '))
    N = int(input('Введите количество столбцов матрицы: '))
    arr = fill_matrix(M, N)

    print('Матрица:')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    print('')

    subArr = [[arr[x][y] for x in range(M)] for y in range(N)]
    for y in range(len(subArr)):
        print('Столбец ', y + 1, ':', sep='')

        amount = 0
        for x in subArr[y]:
            if x > average(subArr[y]):
                amount += 1

        print('Количество элементов, больших среднего арифметического всех элементов этого столбца:', amount, '\n')


def task5():
    print('Задание 4')

    M = int(input('Введите количество строк матрицы: '))
    N = int(input('Введите количество столбцов матрицы: '))
    arr = fill_matrix(M, N)

    print('Матрица:')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    subArr = [[arr[x][y] for x in range(M)] for y in range(N)]
    for y in range(len(subArr)):
        if only_odds(subArr[y]):
            print('Номер первого из ее столбцов, содержащих только нечетные числа:', y + 1)
            return 0
    print(0)


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
