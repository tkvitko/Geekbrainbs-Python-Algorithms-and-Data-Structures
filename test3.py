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

def hex_to_int_list(hex_list):
    # Функция для перевода списка шестнадцатеричных цифр в список десятиных цифр
    num_list = []
    for i in hex_list:
        num_list.append(dict[i])

    return num_list


hex1 = ['5', 'D', '1']
hex2 = ['6', '1', 'F']

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
print(list)

    # Добавляем нули слева для каждой строки
for i, item in enumerate(list):
#    print(f'i={i}')
    for j in range(i):
#        print(f'j={j}')
        item.insert(0, 0)
print(list)

    # Добавляем нули справа для каждоый строки
for i, item in enumerate(list):
    for j in range(len(num2) - i - 1):
        item.append(0)
print(list)

    # Суммирование итоговых строк в столбик
sum_list = []
for j in range(len(list[0])):
    sum_i = 0
    for i in range(len(list)):
        sum_i += list[i][j]
    sum_list.append(sum_i)

    # Обработка итогового списка на предмет чисел больше 15
    #    digit_normalization_hex(sum_list)


print(sum_list)

