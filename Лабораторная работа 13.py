def toFixed(num, digits):
    return f"{num:.{digits}f}"


def task1():
    a = int(input('Введите цену 1 кг конфет: '))

    for x in range(1, 11):
        print('Цена', x / 10, 'кг конфет: ', toFixed(a * x / 10, 2))


def task2():
    N = int(input('Введите целое число N > 0: '))

    multiplication = 1
    x = 1.1
    for i in range(N):
        multiplication *= x
        x += 0.1

    print('Произведение равно', toFixed(multiplication, 3))


def task3():
    N = int(input('Введите целое число N > 0: '))

    amount = 1
    for x in range(3, 2 * N, 2):
        amount += x

    print('N² =', amount)


def task4():
    A = int(input('Введите вещественное число A: '))
    N = int(input('Введите целое число N > 0: '))

    amount = 1
    for i in range(1, N + 1):
        amount += A ** i

    print('Сумма 1 + A + A² + A³ + . . . + A\u207F =', amount)


def task5():
    A = int(input('Введите вещественное число A: '))
    N = int(input('Введите целое число N > 0: '))

    arr = [1]
    for x in range(1, N + 1):
        arr.append(A ** x)

    a = 1
    for x in range(len(arr)):
        arr[x] *= a
        a *= -1

    print('Сумма 1 − A + A² − A³ + . . . ± A\u207F ', sum(arr))


tasks = [task1, task2, task3, task4, task5]
while True:
    tasks[int(input('Перейти к заданию: ')) - 1]()
