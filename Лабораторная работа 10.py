def task1():
    print('Задание 1')

    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))

    print('Неравенство A > 2 и B ≤ 3', end=' ')
    if a > 2 and b <= 3:
        print('справедливо')
    else:
        print('не справедливо')


def task2():
    print('Задание 2')

    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))
    c = int(input('Введите число C: '))

    print('Неравенство A < B < C', end=' ')
    if a < b < c:
        print('справедливо')
    else:
        print('несправедливо')


def task3():
    print('Задание 3')

    a = int(input('Введите число A: '))

    if len(str(a)) == 2 and not a % 2 and a > 0 and type(a) == int:
        print('Данное число является целым четным двузначным')
    else:
        print('Данное число не является четным двузначным')


def task4():
    print('Задание 4')

    a = int(input('Введите число A: '))

    if len(str(a)) != 3:
        print('Число', a, 'не является трехзначным')
        return 0

    for x in str(a):
        if str(a).count(x) != 1:
            print('Цифры числа', a, 'не образуют возрастающую или убывающую последовательность')
            return 0

    if (str(a) == ''.join(sorted(str(a))) or str(a) == ''.join(sorted(str(a)))[::-1]):
        print('Цифры числа', a, 'образуют возрастающую или убывающую последовательность')
    else:
        print('Цифры числа', a, 'не образуют возрастающую или убывающую последовательность')


def task5():
    print('Задание 5')

    a = int(input('Введите число A: '))

    if len(str(a)) != 4:
        print('Число', a, 'не является четырехзначным')
        return 0
    if str(a) == str(a)[::-1]:
        print('Число', a, 'читается одинаково слева направа и справа налево')
    else:
        print('Число', a, 'не читается одинаково слева направа и справа налево')


def task6():
    print('Задание 6')

    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))
    c = int(input('Введите число C: '))

    hypotenuse = max(a, b, c)
    arr = [a, b, c]
    arr.remove(hypotenuse)
    if hypotenuse ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print('Треугольник является прямоугольным')
    else:
        print('Треугольник не является прямоугольным')


def task7(a, b, c):
    print('Задание 7')

    print('Длина стороны A:', a)
    print('Длина стороны B:', b)
    print('Длина стороны C:', c)

    if a >= b + c or b >= a + c or c >= a + b:
        print('Треугольника с заданными сторонами не существует')
        return 0

    print('Треугольник с заданными сторонами существует')


tasks = [task1, task2, task3, task4, task5, task6, task7]
while True:
    tasks[int(input('Перейти к заданию: ')) - 1]()
