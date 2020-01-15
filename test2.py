sum_list = [10, 27, 38, 24]
print(sum_list)

# Приведение суммарной строки от чисел к цифрам
# правило столбика для сложения (количество десятков на предыдущую цифру)

def digit_normalization(sum_list):

    #Магическая функция для превращения списка чисел в список цифр по правилу сложения:
    #если на какой-то позиции число больше 9, от него остается только значение единицы,
    #а значение десятка прибавляется к предыдущему числу

    is_bad_digits = [i for i in sum_list if i > 9]
    # True, если в списке всё ещё есть числа для обработки

    sum_list.insert(0, 0)
    # Добавим лидирующий ноль для случая, если первое число тоже придется обработать

    while is_bad_digits:
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

print(digit_normalization(sum_list))