import sys

n = 2
result = []
while len(result) != 6:
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        result.append(d)
    n += 1
print(result[-1])

# Подсчет использованной памяти
list_of_vars = dict(globals())
memory_used = 0
for k, v in list_of_vars.items():
    memory_used += sys.getsizeof(v)
print(f'Памяти использовано: {memory_used} байт')

print(sys.version)
print(sys.platform)

"""
Самый оптимальный вариант!
Памяти использовано: 902 байт
3.7.3 (default, Sep 18 2019, 14:29:06) 
[Clang 11.0.0 (clang-1100.0.33.8)]
darwin
"""