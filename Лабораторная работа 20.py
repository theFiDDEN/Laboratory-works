def is_unique(arr):
    for x in arr:
        if arr.count(x) != 1:
            return 0
    return 1


def toFixed(num, digits):
    return f"{num:.{digits}f}"


def fill_array(size):
    arr = []
    for x in range(N):
        print('Введите элемент №', x + 1, ' массива: ', end='', sep='')
        arr.append(int(input()))
    return arr


def only_uniques(arr):
    temp = []
    for x in arr:
        if x not in temp:
            temp.append(x)
    return temp


def task1():
    print('Задание 1')

    N = int(input('Введите размер массива: '))
    A = []

    for x in range(N):
        print('Введите элемент №', x + 1, ' массива: ', end='', sep='')
        A.append(int(input()))

    subArr = [[A[0]]]
    for x in A[1:]:
        if x == subArr[-1][-1]:
            subArr[-1].append(x)
        else:
            subArr.append([x])

    B = [len(x) for x in subArr]
    C = [x[0] for x in subArr]

    for x in B:
        print(x, end=' ')

    print('')
    for x in C:
        print(x, end=' ')


def task2():
    print('Задание 2')

    N = int(input('Введите размер массива: '))
    L = int(input('Введите целое число (> 0): '))
    arr = []

    for x in range(N):
        print('Введите элемент №', x + 1, ' массива: ', end='', sep='')
        arr.append(int(input()))

    subArr = [[arr[0]]]
    for x in arr[1:]:
        if x == subArr[-1][-1]:
            subArr[-1].append(x)
        else:
            subArr.append([x])

    subArr = [x if len(x) <= L else [0] for x in subArr]
    arr = [a for b in subArr for a in b]

    print(arr)


def task3():
    print('Задание 3')

    N = int(input('Введите размер массива: '))
    K = int(input('Введите целое число (> 0): '))
    arr = []
    index = 0

    for x in range(N):
        print('Введите элемент №', x + 1, ' массива: ', end='', sep='')
        arr.append(int(input()))

    subArr = [[arr[0]]]
    for x in arr[1:]:
        if x == subArr[-1][-1]:
            subArr[-1].append(x)
        else:
            subArr.append([x])

    for x in range(len(subArr)):
        if len(subArr[x]) > 1:
            index = x

    subArr[K - 1], subArr[index] = subArr[index], subArr[K - 1]
    arr = [a for b in subArr for a in b]

    print(arr)


def task4():
    print('Задание 4')

    N = int(input('Введите количество точек: '))
    A = [[]]

    for x in range(N):
        for y in 'XY':
            print('Введите значение координаты ', y, ' точки ', x + 1, ': ', end='', sep='')
            A[-1].append(int(input()))
        A.append([])

    A = [x for x in A if x and x[0] < 0 and x[1] > 0]

    if not A:
        print('(0, 0)')
        return 0

    A.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)
    A = A[::-1]

    print('Точка во II четверти, наиболее удаленная от начала координат:', A[0])


def task5():
    print('Задание 5')

    N = int(input('Введите количество точек: '))
    A = [[]]
    Triangles = []

    for x in range(N):
        for y in 'XY':
            print('Введите значение координаты ', y, ' точки ', x + 1, ': ', end='', sep='')
            A[-1].append(int(input()))
        A.append([])
    A = [x for x in A if x]

    for a in A:
        for b in A:
            for c in A:
                if is_unique([a, b, c]):
                    side1 = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
                    side2 = ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2) ** 0.5
                    side3 = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) ** 0.5

                    temp = sorted([a, b, c])
                    Triangles.append([temp[0], temp[1], temp[2], float(toFixed(side1 + side2 + side3, 2))])

    Triangles = only_uniques(Triangles)
    Triangles.sort(key=lambda x: x[3])

    temp = [x for x in A if x in Triangles[-1]]
    temp.append(Triangles[-1][-1])

    print('')
    print('Периметр треугольника с наибольшим периметром:', temp[-1])
    print('Его координаты:', temp[0], temp[1], temp[2])


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
