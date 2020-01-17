# Написать алгоритм нахождения i-го по счёту простого числа с помощью алгоритма «Решето Эратосфена».
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import cProfile
import sys

position = 5
end = 100

n = end
sieve = [i for i in range(n)]
sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i * 2
        while j < n:
            sieve[j] = 0
            j += i
result = [i for i in sieve if i != 0]

number = result[position]
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
Памяти использовано: 2142 байт
3.7.3 (default, Sep 18 2019, 14:29:06) 
[Clang 11.0.0 (clang-1100.0.33.8)]
darwin
"""