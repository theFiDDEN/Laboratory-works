import math


def task1(x1, y1, x2, y2):
    print('Координаты точек (', x1, ',', y1, ')', 'и', '(', x2, ',', y2, ')')
    print('Расстояние между ними =', ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

def task2(A, B, C):
    print('Точка A =', A)
    print('Точка B =', B)
    print('Точка C =', C)
    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Сумма длин отрезков AC и BC =', abs(A - C) + abs(B - C))

def task3(A, B, C):
    print('Точка A =', A)
    print('Точка B =', B)
    print('Точка C =', C)
    
    if not a < c < b:
        print('Точка C не расположена между точками A и B')
        return 0
    
    print('Длина отрезка AC =', abs(A - C))
    print('Длина отрезка BC =', abs(B - C))
    print('Произведение длин отрезков AC и BC =', abs(A - C) * abs(B - C))
    
def task4(x1, y1, x2, y2):
    print('Координаты точек (', x1, ',', y1, ')', 'и', '(', x2, ',', y2, ')')
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    print('Периметр прямоугольника =', 2 * (a + b))
    print('Площадь прямоугольника =', a * b)
    
def task5(x1, y1, x2, y2, x3, y3):
    print('Координаты треугольника: (', x1, ',', y1, '),', '(', x2, ',', y2, '),', '(', x3, ',', y3, ')')
    
task5(1, 2, 3, 4, 5, 6)    
