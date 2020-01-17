# Написать алгоритм нахождения i-го по счёту простого числа без помощи алгоритма «Решето Эратосфена».
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import cProfile
import sys

position = 5
end = 100

n = end
all = [i for i in range(n)]
simples = []
not_simples = [0, 1]

for i in all:
    for j in range(2, i - 1):
        if i % j == 0:
            not_simples.append(i)

simples = list(set(all) - set(not_simples))

number = simples[position]

print(number)

# Подсчет использованной памяти
list_of_vars = dict(globals())
memory_used = 0
for k, v in list_of_vars.items():
    memory_used += sys.getsizeof(v)
print(f'Памяти использовано: {memory_used} байт')

print(sys.version)
print(sys.platform)

"""
Памяти использовано: 4822 байт
3.7.3 (default, Sep 18 2019, 14:29:06) 
[Clang 11.0.0 (clang-1100.0.33.8)]
darwin
"""