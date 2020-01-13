# 4. Определить, какое число в массиве встречается чаще всего.

import random

list = [random.randint(1, 10) for i in range(50)]
print(f'Исходный список: {list}')

winner = None
max_count = 0
for i in list:
    count = list.count(i)
    if max_count < count:
        max_count = count
        winner = i
print(f'Число {winner} встречается {max_count} раз')