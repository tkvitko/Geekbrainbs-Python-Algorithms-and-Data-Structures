"""

8. Вводятся три разных числа. Найти,
 какое из них является средним
  (больше одного, но меньше другого).

"""
x = int(input('Пожалуйста, введите первое число: '))
y = int(input('Пожалуйста, введите второе число: '))
z = int(input('Пожалуйста, введите третье число: '))

if x > y:
    if y > z:
        print(f'{y} - среднее')
    else:
        print(f'{z} - среднее')
else:
    if x > z:
        print(f'{x} - среднее')
    else:
        if z > y:
            print(f'{y} - среднее')
        else:
            print(f'{z} - среднее')
