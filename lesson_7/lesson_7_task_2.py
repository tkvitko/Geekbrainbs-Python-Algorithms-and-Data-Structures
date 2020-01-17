# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [random.uniform(0, 50) for i in range(size)]

print(f'Исходный массив: {array}')


def sort_merge(array):
    if len(array) < 2:
        return array
    # Базовый случай для рекурсии

    left = sort_merge(array[:len(array) // 2])
    right = sort_merge(array[len(array) // 2:len(array)])
    # Деление списка на левую и правую часть

    i = 0
    j = 0
    result = []

    # Пройдемся по левой и правой части
    while i < len(left) or j < len(right):
        if i >= len(left):
        # если левая часть пройдена, берем число из правой части
            result.append(right[j])
            j += 1
        elif j >= len(right):
        # если правая часть пройдена, берем число из левой части
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
        # если число из левой части меньше числа из правой, берем его
            result.append(left[i])
            i += 1
        else:
        # если число из правой части меньше числа из левой, берем его
            result.append(right[j])
            j += 1

    return result


print(f'Итоговый массив: {sort_merge(array)}')
