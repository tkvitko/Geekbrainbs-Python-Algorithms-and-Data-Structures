from collections import deque
import sys


N = 500

with open('find_simple_number_var_1.py', 'r', encoding='utf-8') as f:
    strings = deque(f, N)

list_of_strings = []

for item in strings:
    if item.count('=') > 0 and item.count('vars') == 0 and item.count('memory') == 0:
        list_of_strings.append(item)

list_of_vars = []

for item in list_of_strings:
    pos = item.index('=')
    list_of_vars.append(item[:pos])

memory_used = 0

for i in list_of_vars:
    memory_used += sys.getsizeof(i)

print(memory_used)