import timeit
import cProfile

# Алгоритм по нахождению i-го по счету простого числа
def func1(end):
    n = 2
    result = []
    while len(result) != end:
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            result.append(d)
        n += 1
    return result[-1]

def func2(end):
    n = 2
    result = 0
    while n - 2 != end:
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            result = d
        n += 1
    return result

"""
Решето Эратосфена. его принцип в нахождении всех простых чисел до некоторого целого числа n
Как его видоизменить до поставленной задачи, я без понятия, так как в этом случае он уже перестанет быть решетом Эратосфена
А изначально генерировать огромное кол-во чисел, чтобы мы точно оказались в диапазоне, бессмысленно и очевидно это будет не самый быстрый код
"""
def erata(n, sieve):
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]	    # Отсеим нули
    return result

def main(num, alg):
    if alg == 1:
        func1(num)
    elif alg == 2:
        func2(num)
    elif alg == 3:
        lst = [i for i in range(num)]
        lst[1] = 0
        erata(num, lst)

# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(100, 1)"
# 100 loops, best of 5: 3.19 msec per loop
# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(200, 1)"
# 100 loops, best of 5: 15 msec per loop
# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(500, 1)"
# 100 loops, best of 5: 120 msec per loop

# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(100, 2)"
# 100 loops, best of 5: 171 usec per loop
# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(200, 2)"
# 100 loops, best of 5: 558 usec per loop
# python -m timeit -n 100 -s "import les4_task2" "les4_task2.main(500, 3)"
# 100 loops, best of 5: 257 usec per loop

# cProfile.run('main(1000, 1)')
# 1    0.559    0.559    0.559    0.559 les4_task2.py:5(func1)
# cProfile.run('main(10000, 1)')
# 1  113.441  113.441  113.452  113.452 les4_task2.py:5(func1)

# cProfile.run('main(1000, 2)')
# 1    0.011    0.011    0.011    0.011 les4_task2.py:17(func2)
# cProfile.run('main(10000, 2)')
#  1    0.916    0.916    0.916    0.916 les4_task2.py:17(func2)

"""
Решая задачу без генерации нового списка мы гораздо быстрее находим решение, вариант 2 самый быстрый
"""
