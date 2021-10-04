def task1(N):
    print('Задание 1')
    print('С начала суток прошло', N, end=' ')
    if str(N)[-1] == '1':
        print('секунда')
    elif str(N)[-1] in '234':
        print('секунды')
    else:
        print('секунд')

    print('Количество секунд, прошедших с начала последней минуты:', N % 60, end=' ')
    if str(N % 60)[-1] == '1':
        print('секунда')
    elif str(N % 60)[-1] in '234':
        print('секунды')
    else:
        print('секунд')


def task2(K):
    print('Задание 2')
    arr = []
    while len(arr) < 365:
        for x in range(1, 8):
            arr.append(x)
    print('Учитывая, что 1 января - понедельник, номер дня недели ', K, ' дня в году - ', arr[K - 1], sep='')


def task3(N, K):
    print('Задание 3')
    arr = [N]
    while 7 not in arr:
        arr.append(arr[-1] + 1)
    while len(arr) < 365:
        for x in range(1, 8):
            arr.append(x)
    print('Учитывая, что 1 января - ', N, ' день недели, ', K, ' день в году - ', arr[K - 1], ' по счету в неделе',
          sep='')


def task4(A, B, C):
    print('Задание 4')
    print('Дан прямоугольник размером ', A, ' x ', B, sep='')
    print('Максимальное количество квадратов размером ', C, ' x ', C,
          ', которые могут быть помещены в прямоугольнике - ', (A // C) * (B // C), sep='')
    print('Незанятая площадь прямоугольника при помещении в нем максимально возможного количества квадратов - ',
          A * B - (A // C) * (B // C) * C ** 2)


def task5(a):
    print('Задание 5')
    print(a, ' год входит в ', a // 100 + 1, ' столетие', sep='')


task1(67)
print('')

task2(19)
print('')

task3(4, 19)
print('')

task4(3, 9, 2)
print('')

task5(2021)
