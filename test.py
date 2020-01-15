

num1 = [6, 4, 9]
num2 = [4, 2]

list = []

# Умножение в столбик

# 1. Перемножение цифр (полученные строки для последующего сложения добавляем в список)
for j in num2:
    list_j = []
    for i in num1:
        local_comp = i * j
        list_j.append(local_comp)
    list.append(list_j)

print(list)

# Добавляем нули справа для каждой строки
for i, item in enumerate(list):
    for j in range(i):
        item.insert(0, 0)

# Добавляем нули слева для каждоый строки
for i, item in enumerate(list):
    for j in range(len(num2) - i):
        item.append(0)

print(list)

# Суммирование итоговых строк в столбик
sum_list = [0] * (len(num1) + 1)

for i in range(len(num1) + 1):
    sum_list[i] = list[0][i] + list[1][i]

print(sum_list)

is_bad_digits = [i for i in sum_list if i > 9]
# True, если в списке всё ещё есть числа для обработки

while is_bad_digits:
    if sum_list[1] > 9:
        sum_list.insert(0, 0)
        # Добавим лидирующий ноль для случая, если первое число тоже придется обработать
# Приведение суммарной строки от чисел к цифрам
# правило столбика для сложения (количество десятков на предыдущую цифру)
    for i in sum_list:
        if i > 9:
            dec = i // 10
            digit = i % 10
            print(f'i= {i}')
            print(f'dec = {dec}')
            print(f'digit = {digit}')
            cur_pos = sum_list.index(i)
            prev_pos = cur_pos - 1
            sum_list.pop(cur_pos)
            sum_list.insert(cur_pos, digit)
            spam = sum_list.pop(prev_pos)
            sum_list.insert(prev_pos, spam + dec)
        is_bad_digits = [i for i in sum_list if i > 9]

print(sum_list)