# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

size = 10
array = [random.randint(-100, 100) for i in range(size)]

# Тестовые данные (раскоментируйте для проверки 0 итераций, если список уже отсортирован)
# array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f'Исходный массив: {array}')


def is_already_sorted(array):
    # Функция для проверки, отсортирован ли список

    isBigger = []

    for item in range(len(array) - 1):
        if array[item] >= array[item + 1]:
            isBigger.append(True)
        else:
            isBigger.append(False)

    if isBigger.count(False) > 0:
        return False
    else:
        return True


def sort_array_if_not_sorted(array):
    # Функция сортировки пузырьком с оптимизацией:
    # список сортируется до тех пор, пока в этом есть необходимость

    n = 1

    while n < len(array) and is_already_sorted(array) == False:
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

    return n - 1
    # Функция возвращает количество итераций упорядочивания для оценки эффективности


print(f'Количество итераций: {sort_array_if_not_sorted(array)}')
print(array)
