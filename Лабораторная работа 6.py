def task1(a, b):
    print('Входные значения A и B:', a, 'и', b)
    a, b = b, a
    print('Выходные значения A и B:', a, 'и', b)


def task2(a, b, c):
    print('Входные значения A, B и C: ', a, ', ', b, ' и ', c, sep='')
    a, b, c = c, a, b
    print('Выходные значения A, B и C: ', a, ', ', b, ' и ', c, sep='')


def task3(a, b, c):
    print('Входные значения A, B и C: ', a, ', ', b, ' и ', c, sep='')
    a, b, c = b, c, a
    print('Выходные значения A, B и C: ', a, ', ', b, ' и ', c, sep='')


def task4(x):
    print('y(x) =', 3 * x ** 6 - 6 * x ** 2 - 7)


def task5(x):
    print('y(x) =', 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2)


def task6(A):
    temp = A ** 5
    print('A^8 =', temp * A * A * A)


def task7(A):
    temp = A ** 9
    temp1 = A ** 2
    print('A^15 =', temp * temp1 * A * A * A * A)


task1(1, 2)
print('')

task2(1, 2, 3)
print('')

task3(1, 2, 3)
print('')

task4(2)
print('')

task5(2)
print('')

task6(2)
print('')

task7(2)
