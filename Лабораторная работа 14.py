import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('pymorphy2')
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def toFixed(num, digits):
    return f"{num:.{digits}f}"


def task1():
    a = int(input('Введите значение A: '))
    b = int(input('Введите значение B: '))

    if a >= b:
        print('Некорректно введенные данные: A ≥ B')
        return 0

    for x in range(a, b + 1):
        for i in range(x):
            print(x, end=' ')
        print('')


def task2():
    a = int(input('Введите значение A: '))
    b = int(input('Введите значение B: '))
    if a <= b:
        print('Некорректно введенные данные: A ≤ B')
        return 0

    amount = 0
    while amount + b <= a:
        amount += b

    print('Длина незанятой части отрезка A:', a - amount)


def task3():
    n = int(input('Введите значение N: '))
    if n <= 1:
        print('Некорректно введенные данные: N ≤ 1')
        return 0

    amount = [1]
    while sum(amount) < n:
        amount.append(amount[-1] + 1)

    print('K =', amount[-1])


def task4():
    p = int(input('Введите значение P: '))
    if p not in range(0, 26):
        print('Некорректно введенные данные: P ∉ [0, 25]')
        return 0

    i = 0
    amount = 1000
    while amount <= 1100:
        amount *= (p / 100 + 1)
        i += 1

    print('Размер вклада превысит значение 1100 руб. через', i, morph.parse('месяц')[0].make_agree_with_number(i).word)


def task5():
    a = int(input('Введите значение A: '))
    b = int(input('Введите значение B: '))

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print('НОД =', a + b)


def task6():
    arr = [0, 1]
    while len(arr) < 10000:
        arr.append(arr[-2] + arr[-1])

    n = int(input('Введите значение N: '))
    if n <= 1:
        print('Некорректно введенные данные: N ≤ 1')
        return 0
    if n not in arr:
        print('Некорректно введенные данные: N не является числом Фибоначчи')
        return 0

    print('K =', arr.index(n) + 1)
    print(arr[-1])


print('\n', '-' * 300, sep='')
tasks = [task1, task2, task3, task4, task5, task6]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
