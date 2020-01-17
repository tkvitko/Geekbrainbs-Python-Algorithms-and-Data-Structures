import sys

n = 6
m = 3 * n  # задаем размер массива натуральных чисел
prims = []  # массив для хранения простых чисел

#   i = 0
while len(prims) < n:
    prims = []  # обнуляем массив для хранения простых чисел
    nums = list(range(m + 1))  # массив для хранения натуральных чисел
    for i in nums:  # просеиваем nums
        if i > 1:
            for j in range(i + i, len(nums), i):
                nums[j] = 0
    for i in nums:  # заполняем prims
        if i > 1:
            if len(prims) < n:
                prims.append(i)
    m = m * 2  # если nums закончился, а prims еще не наполнился, удваиваем размер nums и пробуем еще раз
print(prims[-1])  # последнее число в массиве и есть искомое

# Подсчет использованной памяти
list_of_vars = dict(globals())
memory_used = 0
for k, v in list_of_vars.items():
    memory_used += sys.getsizeof(v)
print(f'Памяти использовано: {memory_used} байт')

print(sys.version)
print(sys.platform)

"""
Памяти использовано: 1234 байт
3.7.3 (default, Sep 18 2019, 14:29:06) 
[Clang 11.0.0 (clang-1100.0.33.8)]
darwin
"""