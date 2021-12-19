import random


def is_unique(arr):
    for x in arr:
        if arr.count(x) != 1:
            return 0
    return 1


def mean(arr):
    return sum(arr) / len(arr)


def toFixed(num, digits):
    return f"{num:.{digits}f}"


def task1():
    print('Задание 1')

    N = int(input('Введите размер N массивов: '))

    A = [random.randint(1, N) for x in range(N)]
    while not is_unique(A):
        A = [random.randint(1, N) for x in range(N)]
    print('Массив A:', A)

    B = [random.randint(1, N) for x in range(N)]
    while not is_unique(B):
        B = [random.randint(1, N) for x in range(N)]
    print('Массив B:', B)

    A, B = B, A
    print('')
    print('Массив A:', A)
    print('Массив B:', B)


def task2():
    print('Задание 2')

    N = int(input('Введите размер N массивов A и B: '))

    A = [random.randint(1, N) for x in range(N)]
    while not is_unique(A):
        A = [random.randint(1, N) for x in range(N)]
    print('Массив A:', A)

    B = [float(toFixed(mean(A[:x + 1]), 2)) for x in range(N)]
    print('Массив B:', B)


def task3():
    print('Задание 3')

    N = int(input('Введите размер N массива: '))

    arr = [random.randint(1, N) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, N) for x in range(N)]
    print('Массив до изменений:', arr)

    odd = 0
    for x in arr:
        if x % 2:
            odd = x
    print('Последний нечетный элемент:', odd)

    for x in range(len(arr)):
        if arr[x] % 2:
            arr[x] += odd

    print('Массив после изменений:', arr)


def task4():
    print('Задание 4')

    N = int(input('Введите размер N массива: '))

    arr = [random.randint(1, N ** 2) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, N ** 2) for x in range(N)]

    print('Массив до изменений:', arr)

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    for x in range(len(arr)):
        if min_index < x < max_index or max_index < x < min_index:
            arr[x] = 0

    print('Массив после изменений:', arr)


def task5():
    N = int(input('Введите размер N массива: '))

    arr = [random.randint(1, N ** 2) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, N ** 2) for x in range(N)]

    arr[1:] = sorted(arr[1:])
    print('Массив до изменений:', arr)

    arr = sorted(arr)
    print('Массив после изменений:', arr)


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
