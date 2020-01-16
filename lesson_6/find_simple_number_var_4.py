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
