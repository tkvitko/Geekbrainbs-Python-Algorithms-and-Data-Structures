# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

list.pop(pos_of_min)
list.insert(pos_of_min, max_item)
list.pop(pos_of_max)
list.insert(pos_of_max, min_item)

print(f'Итоговый список: {list}')
