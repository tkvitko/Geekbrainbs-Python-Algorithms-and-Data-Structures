# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# вводные
a = 5
b = 6
shift = 2

# вычисления
result_and = a & b
result_or = a | b
result_xor = a ^ b
result_not_a = ~ a
result_not_b = ~ b
result_right = a >> shift
result_left = a << shift

# вывод результатов
print(f'Битовое И для {a} и {b}: {result_and}')
print(f'Битовое ИЛИ для {a} и {b}: {result_or}')
print(f'Битовое исключающее ИЛИ для {a} и {b}: {result_xor}')
print(f'Битовое отрицание {a}: {result_not_a}')
print(f'Битовое отрицание {b}: {result_not_b}')
print(f'Побитовый сдвиг вправо на {shift} знака для {a}: {result_right}')
print(f'Побитовый сдвиг вправо на {shift} знака для {a}: {result_left}')
