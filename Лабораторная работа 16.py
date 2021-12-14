import random
import math


def toFixed(num, digits):
    return f"{num:.{digits}f}"


def task1():
    print('Задание 1')

    N = int(input('Введите размер массива N: '))

    arr = [1]
    while len(arr) < N:
        arr.append(arr[-1] + 2)

    print(arr)


def task2():
    print('Задание 2')

    N = int(input('Введите размер массива N: '))
    A = int(input('Введите первый элемент A: '))
    D = int(input('Введите знаменатель D: '))

    arr = [A]
    while len(arr) < N:
        arr.append(arr[-1] * D)

    print(arr)


def task3():
    print('Задание 3')

    N = int(input('Введите размер массива N: '))
    A = int(input('Введите первый элемент A: '))
    B = int(input('Введите второй элемент B: '))

    arr = [A, B]

    while len(arr) < N:
        arr.append(sum(arr))

    print(arr)


def task4():
    print('Задание 4')

    N = int(input('Введите размер массива N: '))
    A = []
    arr = []

    while len(A) < N:
        A.append(random.randint(1, 1000))

    print(A)

    while len(A):
        arr.append(A[0])
        A.remove(A[0])

        if len(A):
            arr.append(A[-1])
            A.remove(A[-1])

    print(arr)


def task5():
    print('Задание 5')

    N = int(input('Введите размер массива N: '))
    arr = []

    while len(arr) < N:
        arr.append(random.randint(1, 1000))

    print(arr)
    print([arr[x] for x in range(len(arr)) if not x % 2])
    print([arr[x] for x in range(len(arr)) if x % 2][::-1])


print('\n', '-' * 300, sep='')
tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
