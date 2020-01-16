# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

min_item = 0
max_item = 10

list = [random.randint(min_item, max_item) for i in range(20)]
print(f'Исходный список: {list}')


def find_and_remove_min(list):
    min = 10
    pos_of_min = 0

    for i in list:
        if min > i:
            min = i
        pos_of_min = list.index(min)

    list.pop(pos_of_min)
    print(min)
    return min


count = int(input('Сколько минимальных хотите найти? '))

for i in range(count):
    find_and_remove_min(list)
