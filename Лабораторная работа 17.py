import random
import math


def toFixed(num, digits):
    return f"{num:.{digits}f}"


def is_unique(arr):
    for x in arr:
        if arr.count(x) != 1:
            return 0
    return 1


def task1():
    print('Задание 1')

    N = int(input('Введите размер массива N: '))
    K = int(input('Введите значение K: '))
    L = int(input('Введите значение L: '))

    arr = [random.randint(1, 100) for x in range(N)]
    print('Массив:', arr)
    print('Элементы массива с номерами от', K, 'до', L, ':', arr[K - 1:L])

    print('\n', '-' * 300, sep='')


def task2():
    print('Задание 2')

    N = int(input('Введите размер массива N: '))

    temp = int(input('Ввести элементы вручную? 1 - Да, 0 - нет '))
    arr = []

    if not temp:
        arr = [random.randint(1, N) for x in range(N)]
        while not is_unique(arr):
            arr = [random.randint(1, N) for x in range(N)]
        print(arr)
    else:
        for x in range(N):
            print('Введите элемент', x + 1, 'массива N: ', end='')
            arr.append(int(input()))

    for x in range(1, len(arr)):
        if arr[x] < arr[x - 1]:
            print('0')
            return 0

    print('Разность прогрессии:', arr[-1] - arr[0])


def task3():
    print('Задание 3')

    N = int(input('Введите размер массива N: '))
    arr = [random.randint(1, N) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, N) for x in range(N)]

    for x in range(len(arr)):
        print(x + 1, ') ', arr[x], sep='')

    print('Минимальный элемент из элементов массива с четными номерами: A2, A4, A6 -', min(arr[1], arr[3], arr[5]))


def task4():
    print('Задание 4')

    N = int(input('Введите размер массива N: '))
    arr = [random.randint(1, 1000) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, 1000) for x in range(N)]

    for x in range(len(arr)):
        print(x + 1, ') ', arr[x], sep='')

    local_max = 0
    for x in range(1, len(arr) - 1):
        if arr[x - 1] < arr[x] > arr[x + 1]:
            local_max = x + 1

    print('Номер последнего локального максимума массива:', local_max)


def task5():
    print('Задание 5')

    N = int(input('Введите размер массива N: '))
    arr = [random.randint(1, N) for x in range(N)]
    while not is_unique(arr):
        arr = [random.randint(1, N) for x in range(N)]

    arr[random.randint(1, N - 1)] = arr[random.randint(1, N - 1)]
    while is_unique(arr):
        arr[random.randint(1, N - 1)] = arr[random.randint(1, N - 1)]

    for x in range(len(arr)):
        print(x + 1, ') ', arr[x], sep='')

    nums = []
    for x in range(len(arr)):
        if arr.count(arr[x]) == 2:
            nums.append(x + 1)

    print('Номера двух одинаковых элементов:', nums[0], 'и', nums[1])


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
