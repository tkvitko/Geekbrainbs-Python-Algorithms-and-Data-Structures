from collections import deque

def digit_normalization_hex(sum_list):
    #Магическая функция для превращения списка чисел в список цифр по правилу сложения:
    #если на какой-то позиции число больше 15, от него остается только значение единицы,
    #а значение десятка прибавляется к предыдущему числу

    #Применяется далее для того, чтобы привести нижнюю (итоговую) строчку столбика к виду,
    #когда в нем только цифры

    is_bad_digits = [i for i in sum_list if i > 15]
    # True, если в списке всё ещё есть числа для обработки

    while is_bad_digits:
        if sum_list[0] > 15:    #был баг с 1 вместо 0, проверялся не тот элемент
            sum_list.insert(0, 0)
            # Добавим лидирующий ноль для случая, если первое число тоже придется обработать
        for i in sum_list:
            if i > 15:
                dec = i // 16
                digit = i % 16
                cur_pos = sum_list.index(i)
                prev_pos = cur_pos - 1
                sum_list.pop(cur_pos)
                sum_list.insert(cur_pos, digit)
                spam = sum_list.pop(prev_pos)
                sum_list.insert(prev_pos, spam + dec)
            is_bad_digits = [i for i in sum_list if i > 15]

    return sum_list


def composition_hex(hex1, hex2):
    # Функция для умножения в столбик двух шестнадцатеричных чисел, представленных списком цифр

    # Преобразуем входные списки шестнадцатеричных цифр в списки десятичных цифр
    num1 = hex_to_int_list(hex1)
    num2 = hex_to_int_list(hex2)

    # Умножение в столбик
    list = []

    for j in num2:
        list_j = []
        for i in num1:
            local_comp = i * j
            list_j.append(local_comp)
        list.append(list_j)

    # Добавляем нули слева для каждой строки
    for i, item in enumerate(list):
        for j in range(i):
            item.insert(0, 0)

    # Добавляем нули справа для каждоый строки
    for i, item in enumerate(list):
        for j in range(len(num2) - i - 1):  #был баг с невычитаением 1, что приводило к лишнему нулю
            item.append(0)

    # Суммирование итоговых строк в столбик
    sum_list = []
    for j in range(len(list[0])):
        sum_i = 0
        for i in range(len(list)):
            sum_i += list[i][j]
        sum_list.append(sum_i)

    # Обработка итогового списка на предмет чисел больше 15
    digit_normalization_hex(sum_list)

    return sum_list


def summa_hex(hex1, hex2):
    # Функция для сложения в столбик двух шестнадцатеричных чисел, представленных списком цифр

    # Преобразуем входные списки шестнадцатеричных цифр в списки десятичных цифр
    num1 = hex_to_int_list(hex1)
    num2 = hex_to_int_list(hex2)

    # Приведение строк к равной длине
    dif = abs(len(num1) - len(num2))
    if dif:
        if len(num1) < len(num2):
            for i in range(dif):
                num1.insert(0, 0)
        else:
            for i in range(dif):
                num2.insert(0, 0)

    # Сложение в столбик
    summ = []

    for i in range(len(num1)):
        sum = num1[i] + num2[i]
        summ.append(sum)

    # Обработка итогового списка на предмет чисел больше 15
    digit_normalization_hex(summ)

    return summ


def hex_to_int_list(hex_list):
    # Функция для перевода списка шестнадцатеричных цифр в список десятиных цифр
    num_list = []
    for i in hex_list:
        num_list.append(dict[i])

    return num_list


def int_to_hex_list(num_list):
    # Функция для перевода списка десятичных цифр в список шестнадцатеричных цифр
    hex_list = []
    for i in num_list:
        def dict_search(num):
            for k, v in dict.items():
                if v == num:
                    return k
        j = dict_search(i)
        hex_list.append(j)

    return hex_list


# Словарь соответствия шестнадцатеричных цифр десятичным
dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


#Вводные
#hex1 = ['C', '4', 'F']
#hex2 = ['A', '2']

#Вводные
#hex1 = ['5', 'D', '1']
#hex2 = ['6', '1', 'F']
# Сумма: ['B', 'F', '0']
# Произведение: ['2', '3', '9', 'A', '4', 'F']

string1 = input('Первое число: ')
string2 = input('Второе число: ')
hex1 = list(string1)
hex2 = list(string2)

print(f'Сумма: {int_to_hex_list(summa_hex(hex1, hex2))}')
print(f'Произведение: {int_to_hex_list(composition_hex(hex1, hex2))}')
