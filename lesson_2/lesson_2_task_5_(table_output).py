# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

start_index = 32
end_index = 127
number_in_string = 10

for i in range(start_index, end_index + 1):
    number_in_string -= 1
    if number_in_string != 0:
        print(f'{i} {chr(i)}', end=' ')
    else:
        print(f'{i} {chr(i)}')
        number_in_string = 10
