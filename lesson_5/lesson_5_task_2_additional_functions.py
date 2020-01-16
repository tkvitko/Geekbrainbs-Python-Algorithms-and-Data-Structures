def digit_normalization(sum_list):
    # Не пригодилась (это для десятичных)
    # Магическая функция для превращения списка чисел в список цифр по правилу сложения:
    # если на какой-то позиции число больше 9, от него остается только значение единицы,
    # а значение десятка прибавляется к предыдущему числу

    is_bad_digits = [i for i in sum_list if i > 9]
    # True, если в списке всё ещё есть числа для обработки

    while is_bad_digits:
        if sum_list[1] > 9:
            sum_list.insert(0, 0)
            # Добавим лидирующий ноль для случая, если первое число тоже придется обработать
        for i in sum_list:
            if i > 9:
                dec = i // 10
                digit = i % 10
                cur_pos = sum_list.index(i)
                prev_pos = cur_pos - 1
                sum_list.pop(cur_pos)
                sum_list.insert(cur_pos, digit)
                spam = sum_list.pop(prev_pos)
                sum_list.insert(prev_pos, spam + dec)
            is_bad_digits = [i for i in sum_list if i > 9]

    return sum_list


def composition(num1, num2):
    # Функция для умножения в столбик двух десятичных чисел, представленных списком цифр

    # Умножение в столбик
    list = []

    for j in num2:
        list_j = []
        for i in num1:
            local_comp = i * j
            list_j.append(local_comp)
        list.append(list_j)

    # Добавляем нули справа для каждой строки
    for i, item in enumerate(list):
        for j in range(i):
            item.insert(0, 0)

    # Добавляем нули слева для каждоый строки
    for i, item in enumerate(list):
        for j in range(len(num2) - i):
            item.append(0)

    # Суммирование итоговых строк в столбик
    sum_list = [0] * (len(num1) + 1)
    for i in range(len(num1) + 1):
        sum_list[i] = list[0][i] + list[1][i]

    # Обработка итогового списка на предмет чисел больше 9
    # (с помощью другой функции)
    digit_normalization(sum_list)

    return sum_list


def summa(num1, num2):
    # Функция для сложения в столбик двух десятичных чисел, представленных списком цифр

    # Приведение строк к равно длине
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

    # Обработка итогового списка на предмет чисел больше 9
    # (с помощью другой функции)
    digit_normalization(summ)

    return summ


def hex_to_dec(string):
    # Функция перевода шестнадцатеричной цифры в десятичную

    num = dict[string]
    return num


def dec_to_hex(num):
    # Функция перевода десятичной цифры в шестнадцатеричную

    for k, v in dict.items():
        if v == num:
            return k


num1 = [2, 3, 4]
num2 = [5, 6, 7]

print(summa(num1, num2))
print(composition(num1, num2))
