# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

list = list(set([random.randint(-100, 100) for i in range(30)]))
print(f'Исходный список: {list}')

max_negative = -100
position_of_max = 0

for i in list:
    if i < 0:
        if max_negative < i:
            max_negative = i
            position_of_max = list.index(i)

print(f'Максимальный отрицательный элемент {max_negative} находитс на позиции {position_of_max}')
