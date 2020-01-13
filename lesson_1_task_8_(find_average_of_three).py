# 8. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).


a = int(input('Введите число: '))
b = int(input('Введите другое число: '))
c = int(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c:
            avg = b
        elif b < c:
            avg = c
    elif a < c:
        avg = a
elif a < b:
    if a > c:
        avg = a
    elif a < c:
        if b > c:
            avg = c
        elif b < c:
            avg = b

print(f'Среднее: {avg}')
