# 7. Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import random

def way1(n):
    number = 0
    sum = 0
    for i in range(n):
        next_number = number + 1
        sum = sum + next_number
        number = next_number
    return sum

def way2(n):
    return int((n*(n+1)/2))

#Проврека пользователем
user_number = int(input('Введите число для проверки: '))
print(f'Значение формулы 1: {way1(user_number)}')
print(f'Значение формулы 2: {way2(user_number)}')

#Доказательство
test = random.randint(0, 100000)
if way1(test) == way2(test):
    print(f'Все хорошо (проверено на {test})')
else:
    print('Что-то не так')

