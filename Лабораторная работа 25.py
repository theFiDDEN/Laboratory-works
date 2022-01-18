def task1():
    print('Задание 1')

    read = open('1.txt', 'r', encoding='utf-8').read()
    write = open('1.txt', 'w', encoding='utf-8').write(read[read.index(' ') + 1:])


def task2():
    print('Задание 2')

    name = input('Введите имя нового файла: ')
    if '.txt' not in name:
        name += '.txt'

    N = int(input('Введите количество строк: '))
    K = int(input('Введите количество символов «*» в каждой строке: '))

    my_file = open(name, 'w', encoding='utf-8')
    my_file.write(N * (K * '*' + '\n'))
    my_file.close()


def task3():
    print('Задание 3')

    file1_read = open('1.txt', 'r', encoding='utf-8').read()
    file2_read = open('2.txt', 'r', encoding='utf-8').read()
    file1_write = open('1.txt', 'w', encoding='utf-8').write(file2_read + file1_read)


def task4():
    print('Задание 4')

    read = open('1.txt', 'r', encoding='utf-8').read()
    for x in range(read.count(' '), 1, -1):
        read = read.replace(' ' * x, ' ')

    write = open('1.txt', 'w', encoding='utf-8').write(read)


def task5():
    print('Задание 5')

    read = open('1.txt', 'r', encoding='utf-8').read()

    read = read.split('\n')
    for x in range(len(read)):
        read[x] = read[x].replace('\n', '')
        read[x] = read[x].rstrip()

    read = [x for x in read if x and x.index(' ' * 5) == 0]

    print(read)

    print('Количество абзацев в файле:', len(read))


tasks = [task1, task2, task3, task4, task5]
while True:
    print('')
    tasks[int(input('Перейти к заданию: ')) - 1]()
