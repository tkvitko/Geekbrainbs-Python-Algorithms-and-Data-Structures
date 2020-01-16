# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введите натуральное число: '))
even_count = 0
uneven_count = 0

while number > 0:
    digit = number % 10
    number //= 10
    if digit % 2 == 0:
        # Альтернативный поиск:
        #    if digit in [0, 2, 4, 6, 8]:
        even_count += 1
    else:
        uneven_count += 1

print(f'Количество четных: {even_count}')
print(f'Количество нечетных: {uneven_count}')
