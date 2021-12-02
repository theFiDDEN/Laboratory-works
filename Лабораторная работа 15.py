import math
import random


def PowerA3(A):
    B = A ** 3
    return B


def Sign(X):
    if X < 0:
        return -1
    elif X == 0:
        return 0
    elif X > 0:
        return 1


def RingS(R1, R2):
    arr = sorted([R1, R2])
    R1 = arr[0]
    R2 = arr[1]

    return math.pi * (R2 ** 2 - R1 ** 2)


def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


def Fact2(N):
    amount = 1

    for i in range(1 + int(not N % 2), N + 1, 2):
        amount *= i

    return amount


print('PowerA3:')
for i in range(5):
    temp = random.uniform(1, 30)
    print(' ' * 3, temp, '³ = ', PowerA3(temp), sep='')

print('\nSign:')
temp1 = random.randint(-20, 20)
temp2 = random.randint(-20, 20)
print('Sign(', temp1, ') + Sign(', temp2, ') = ', Sign(temp1) + Sign(temp2), sep='')

print('\nRingS:')
for i in range(3):
    temp1 = random.randint(1, 20)
    temp2 = random.randint(1, 20)
    print('Площадь кольца, заключенного между двумя окружностями с общим центром и радиусами', temp1, 'и', temp2,
          'равна', RingS(temp1, temp2))

print('\nQuarter:')
for i in range(3):
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    print('Точка (', x, ', ', y, ') находится в ', Quarter(x, y), ' четверти', sep='')

print('\nFact2:')
for i in range(3):
    temp = random.randint(1, 100)
    print(temp, '!! = ', Fact2(temp), sep='')
