import random


def is_unique(arr):
    for x in arr:
        if arr.count(x) != 1:
            return 0
    return 1


def fill_matrix():
    M = int(input('Введите количество строк матрицы: '))
    N = int(input('Введите количество столбцов матрицы: '))
    arr = []

    while not arr or not is_unique([a for b in arr for a in b]):
        arr.clear()
        for x in range(M):
            arr.append([])
            for y in range(N):
                arr[-1].append(random.randint(0, 100))

    return arr


def task1():
    print('Задание 1')

    arr = fill_matrix()

    print('Матрица до изменений')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    for x in range(len(arr)):
        maximum = 0
        minimum = 0
        for y in range(len(arr[x])):
            if arr[x][y] == max(arr[x]):
                maximum = y
            if arr[x][y] == min(arr[x]):
                minimum = y
        arr[x][maximum], arr[x][minimum] = arr[x][minimum], arr[x][maximum]

    print('\n', 'Поменять местами максимальный и минимальный элемент каждой строки:', sep='')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')


def task2():
    print('Задание 2')

    arr = fill_matrix()
    min_index = 0
    max_index = 0

    print('Матрица до изменений')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == max([a for b in arr for a in b]):
                max_index = y
            if arr[x][y] == min([a for b in arr for a in b]):
                min_index = y

    for x in range(len(arr)):
        arr[x][max_index], arr[x][min_index] = arr[x][min_index], arr[x][max_index]

    print('\n', 'Минимальный элемент матрицы: ', min([a for b in arr for a in b]), sep='')
    print('Максимальный элемент матрицы: ', max([a for b in arr for a in b]))

    print('\n', 'Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы:', sep='')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')


def task3():
    print('Задание 3')

    arr = fill_matrix()

    print('Матрица до изменений')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if (x + 1) <= len(arr) // 2 and (y + 1) <= len(arr[x]) // 2:
                arr[x][y], arr[len(arr) // 2 + x][len(arr[x]) // 2 + y] = arr[len(arr) // 2 + x][len(arr[x]) // 2 + y], \
                                                                          arr[x][y]

    print('\n', 'Поменять местами левую верхнюю и правую нижнюю четверти матрицы:', sep='')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')


def task4():
    print('Задание 4')

    arr = fill_matrix()

    print('Матрица до изменений')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    arr.sort(key=lambda x: x[0])

    print('\n', 'Упорядочить ее строки так, чтобы их первые элементы образовывали возрастающую последовательность:',
          sep='')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')


def task5():
    print('Задание 5')

    arr = fill_matrix()
    sums = []

    print('Матрица до изменений')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print('')

    for first_y in range(1, len(arr[0])):
        x = 0
        temp = []
        for y in range(first_y, len(arr[0])):
            temp.append(arr[x][y])
            x += 1
        sums.insert(0, sum(temp))

    sums.append('')

    for first_x in range(1, len(arr)):
        y = 0
        temp = []
        for x in range(first_x, len(arr)):
            temp.append(arr[x][y])
            y += 1
        sums.append(sum(temp))

    print('\n', 'Найти сумму элементов диагонали матрицы, параллельной главной:', sep='')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print('{:>3}'.format(arr[x][y]), end=' ')
        print(' | ', sums[0], end='')
        sums.remove(sums[0])
        print('')

    sums = sums[::-1]
    print(' -- ' * len(arr))
    for x in range(len(sums)):
        if sums[0]:
            print('{:>3}'.format(sums[0]), end=' ')
            sums.remove(sums[0])


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
