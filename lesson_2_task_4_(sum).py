# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

len = int(input('Введите длину ряда: '))
number = 1
#sum = 1
sum = 0

#for i in range(len - 1):
#    next_number = number / (-2)
#    sum = sum + next_number
#    number = next_number
for i in range(len):
    sum = sum + number
    number = number / (-2)

print(sum)