# Задание 6
# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_6_task_1, les_6_task_2, и т.д.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.
import platform
from random import randint
import sys
from sys import getsizeof

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

array_len = 10

def show_total_size(dictionary):
    def get_size(x):
        size = getsizeof(x)
        if type(x) is list:
            print(f'Size of {x} = {size} bytes')
            for i in x:
                size_i = getsizeof(i)
                size += size_i
                print(f'\tSize of {i} = {size_i} bytes')
            print(f'\tОбщий размер массива = {size} bytes')
        elif type(x) is int:
            print(f'Size of {x} = {size} bytes')
        return size

    print('\nИспользуемые переменные: ')
    [print('\t', x, '=', dictionary[x], type(dictionary[x])) for x in dictionary]
    print()

    total_size = 0
    for x in dictionary:
        total_size += get_size(dictionary[x])
    return total_size

# Первый способ:

def first(array):
    min_pos = 0
    max_pos = 0
    for i in range(1, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
        elif array[i] > array[max_pos]:
            max_pos = i

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array, show_total_size(locals())

# Второй способ:

def second(array):
    min_pos = array.index(min(array))
    max_pos = array.index(max(array))

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array, show_total_size(locals())

lst = [randint(0, 49) for _ in range(array_len)]
answer = first(lst)
print(f'Для выполнения кода потребовалось {answer[1]} bytes памяти\n')
print(f'Итог выполнения кода: {answer[0]}')

print('*' * 100)

answer = second(lst)
print(f'Для выполнения кода потребовалось {answer[1]} bytes памяти\n')
print(f'Итог выполнения кода: {answer[0]}')

# Вывод: второй вариант потребовал меньше памяти, чем первый.
# Комментарии в формате значений занимаемой памяти выводятся после запуска кода.

print('*' * 100)
print(sys.version, sys.platform)
print(platform.architecture())