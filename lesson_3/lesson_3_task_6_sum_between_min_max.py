# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

max_item = 0
min_item = 100

list = list(set([random.randint(max_item, min_item) for i in range(10)]))
print(f'Исходный список: {list}')

for i in list:
    if max_item < i:
        max_item = i
    if min_item > i:
        min_item = i

print(f'Минимальное: {min_item}, максимальное: {max_item}')

pos_of_min = list.index(min_item)
pos_of_max = list.index(max_item)
print(f'Позиция минимального: {pos_of_min}, позиция максимального: {pos_of_max}')

if pos_of_min < pos_of_max:
    new_list = list[pos_of_min + 1:pos_of_max]
else:
    new_list = list[pos_of_max + 1:pos_of_min]

print(f'Список элементов между минимальным и максимальным: {new_list}')

sum = 0
for i in new_list:
    sum += i

print(f'Сумма элементов между минимальным и максимальным: {sum}')
