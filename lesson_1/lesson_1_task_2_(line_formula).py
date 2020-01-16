# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

# ввод данных
x1 = int(input('Введите X1: '))
y1 = int(input('Введите Y1: '))
x2 = int(input('Введите X2: '))
y2 = int(input('Введите Y2: '))

# вычисления
if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    # вывод результатов
    print(f'Уравнение: y = {k}x + {b}')
else:
    print(f'Уравнение: x = {x1}')
