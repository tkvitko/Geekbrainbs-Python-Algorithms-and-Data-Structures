# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

len = int(input('Введите длину ряда: '))
number = 1
sum = 0

for i in range(len):
    sum = sum + number
    number = number / (-2)

print(sum)


# Вариант решения через рекурсию (от другого студента)
# k - количество элементов
# itog - текущее значение суммы, на входе в рекурисию равно 1
def recursion(k, itog):
    k -= 1
    if k > 0:
        itog += (-0.5) * recursion(k, itog)
    return itog


print(recursion(4, 1))
