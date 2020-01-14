# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex1 = ['A', '2']
hex1 = deque(hex1)
hex2 = ['C', '4', 'F']
hex2 = deque(hex2)

# Приведение чисел в одной длине
dif = abs(len(hex1) - len(hex2))
if dif:
    if len(hex1) < len(hex2):
        for i in range(dif):
            hex1.appendleft('0')
    else:
        for i in range(dif):
            hex2.appendleft('0')

# Словарь соответствия цифр
dict = {
        'A': 4,
        'B': 5,
        'C': 6,
        'D': 7,
        'E': 8,
        'F': 9,
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

#Функция перевода 16 в 10
def hex_to_dec(string):
    num = dict[string]
    return num


#Функция перевода 10 в 16
def dec_to_hex(num):
    for k, v in dict.items():
        if v == num:
            return k


num1 = deque()
num2 = deque()

#Переведем цифры из 16 в 10
for i in hex1:
      num1.append(hex_to_dec(i))
for i in hex2:
      num2.append(hex_to_dec(i))
print(num1)
print(num2)

summ = []

#Просуммируем
for i in range(len(num1)):
    sum = num1[i] + num2[i]
    summ.append(sum)
print(summ)

#Применим правило столбика (десяток на предыдущую цифру)
for i in summ:
    if i > 9:
        diff = i - 10
        cur_pos = summ.index(i)
        prev_pos = cur_pos - 1
        summ.pop(cur_pos)
        summ.insert(cur_pos, diff)
        spam = summ.pop(prev_pos)
        summ.insert(prev_pos, spam + 1)

print(summ)

#Преобразуем цифры из 10 обратно в 16
summ_hex = []
for i in summ:
      summ_hex.append(dec_to_hex(i))
print(summ_hex)

