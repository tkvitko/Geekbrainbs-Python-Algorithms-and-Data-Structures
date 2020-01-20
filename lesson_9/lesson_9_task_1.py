# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

import hashlib

str = input('Введите строку для анализа: ')


def count_uniq_substrings(string):
    hashs_full_list = []
    # пустой список для хранения хешей всех подстрок

    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            hashs_full_list.append(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    # заполняем список хешами всех подстрок (неуникальных)

    hashs_uniq_list = list(set(hashs_full_list))
    # исключаем одинаковые хеши

    result = len(hashs_uniq_list) - 2
    # вычитаем нулевую и полную строку

    return result


print(f'{count_uniq_substrings(str)} уникальных подстрок')
