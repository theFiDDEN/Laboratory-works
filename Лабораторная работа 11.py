def toFixed(num, digits):
    return f"{num:.{digits}f}"


def task1():
    print('Задание 1')
    print('')

    a = int(input('Введите целое значение A: '))
    b = int(input('Введите целое значение B: '))
    print('')

    if a != b:
        a = max(a, b)
        b = max(a, b)

    print('Новое значение A:', a)
    print('Новое значение B:', b)


def task2():
    print('Задание 2')
    print('')

    a = int(input('Введите значение A: '))
    b = int(input('Введите значение B: '))
    c = int(input('Введите значение C: '))
    print('')

    arr = sorted([a, b, c])[::-1]

    print('Сумма двух наибольших значений:', arr[0] + arr[1])


def task3():
    print('Задание 3')
    print('')

    A = [int(input('Введите значение координаты X для точки A: ')),
         int(input('Введите значение координаты Y для точки A: '))]

    print('')

    B = [int(input('Введите значение координаты X для точки B: ')),
         int(input('Введите значение координаты Y для точки B: '))]

    print('')

    C = [int(input('Введите значение координаты X для точки C: ')),
         int(input('Введите значение координаты Y для точки C: '))]

    print('')

    AB = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    AC = ((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2) ** 0.5

    if AB < AC:
        print('Точка B ближе расположена ближе к точке A, чем точка C')
        print('Расстояние от точки B до точки A:', toFixed(AB, 2))
    else:
        print('Точка C ближе расположена ближе к точке A, чем точка B')
        print('Расстояние от точки C до точки A:', toFixed(AC, 2))


def task4():
    print('Задание 4')
    print('')

    x = int(input('Введите значение координаты X для точки A: '))
    y = int(input('Введите значение координаты Y для точки A: '))
    print('')

    if x > 0 and y > 0:
        print('Точка A расположена в I четверти')
    elif x < 0 and y > 0:
        print('Точка A расположена во II четверти')
    elif x < 0 and y < 0:
        print('Точка A расположена в III четверти')
    elif x > 0 and y < 0:
        print('Точка A расположена в IV четверти')


def task5():
    print('Задание 5')

    a = int(input('Введите целое число A: '))

    print('Число A', end=' ')
    if a < 0:
        print('отрицательное', end=' ')
    if a == 0:
        print('нулевое')
        return 0
    if a > 0:
        print('положительное', end=' ')
    if not a % 2:
        print('четное')
    if a % 2:
        print('нечетное')


def task6():
    print('Задание 6')

    a = int(input('Введите целое число A в диапазоне 1 - 999: '))

    print('Число A', end=' ')
    if not a % 2:
        print('четное')
    if a % 2:
        print('нечетное')
    if 1 <= a <= 9:
        print('однозначное')
    if 10 <= a <= 99:
        print('двузначное')
    if 100 <= a <= 999:
        print('трехзначное')


tasks = [task1, task2, task3, task4, task5, task6]
while True:
    tasks[int(input('Перейти к заданию: ')) - 1]()
