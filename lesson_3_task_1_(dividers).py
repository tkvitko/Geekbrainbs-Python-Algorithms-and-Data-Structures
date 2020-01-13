# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

numbers_list = [i for i in range(2, 100)]
dividers_list = [i for i in range(2, 10)]

for j in dividers_list:
    multiple_of_j = 0
    for i in numbers_list:
        if i % j == 0:
            multiple_of_j += 1
    print(f'На {j} делится {multiple_of_j} чисел (числа)')