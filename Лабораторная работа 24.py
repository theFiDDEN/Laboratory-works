def task1():
    print('Задание 1')

    str = input('Введите строку: ')
    arr = str.split()

    print('Количество слов в строке:', len(arr))


def task2():
    print('Задание 2')

    str = input('Введите строку: ')
    arr = str.split()

    print('Длина самого короткого слова:', len(min(arr, key=len)))


def task3():
    print('Задание 3')

    str = input('Введите строку: ')
    arr = str.split()
    newArr = []

    newStr = [str[0]]
    letter = str[0] if 1040 <= ord(str[0]) <= 1071 else ''
    for x in range(1, len(str)):
        newStr.append(str[x])
        if str[x - 1] == ' ' and 1040 <= ord(str[x]) <= 1071:
            letter = str[x]
            continue
        if str[x] == letter:
            newStr[-1] = '.'
    newStr = ''.join(newStr)

    print(newArr)

    print(
        'Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы на символ «.» (точка):')
    print(newStr)


def task4():
    print('Задание 4')

    str = input('Введите строку: ')
    amount = 0

    for x in str:
        if x in 'ауоыэяюёие' or x in 'АУОЫЭЯЮЁИЕ':
            amount += 1

    print('Количество содержащихся в строке гласных букв:', amount)


def task5():
    print('Задание 5')

    str = input('Введите адрес файла: ')

    for x in range(len(str) - 1, 0, -1):
        if str[x] == '.':
            str = str[:x]
            break

    for x in range(len(str) - 1, 0, -1):
        if str[x] == chr(92):
            str = str[x + 1:]
            break

    print('Выделить из этой строки имя файла (без расширения):', str)


def task6():
    print('Задание 6')

    str = input('Введите адрес файла: ')

    for x in range(len(str) - 1, 0, -1):
        if str[x] == chr(92):
            str = str[:x]
            break

    for x in range(len(str) - 1, 0, -1):
        if str[x] == chr(92):
            str = str[x + 1:]
            break

    print('Выделить из этой строки название последнего каталога:', str)


def task7():
    print('Задание 7')

    str = input('Введите строку: ')
    odd = ''
    even = ''
    newStr = ''

    for x in range(len(str)):
        if (x + 1) % 2:
            odd += str[x]
        else:
            even += str[x]

    newStr = even + odd[::-1]

    print(newStr)


tasks = [task1, task2, task3, task4, task5, task6, task7]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
