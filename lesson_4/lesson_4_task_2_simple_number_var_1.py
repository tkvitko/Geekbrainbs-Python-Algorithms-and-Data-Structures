# Написать алгоритм нахождения i-го по счёту простого числа с помощью алгоритма «Решето Эратосфена».
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import cProfile

def find_simple(position, end):

    def create_simples():
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
        return result
    list = create_simples()
    number = list[position]
    return number

# "lesson_4_task_2_var_1.find_simple(10, 100)"
# 1000 loops, best of 5: 28.6 usec per loop

# "lesson_4_task_2_var_1.find_simple(20, 100)"
# 1000 loops, best of 5: 29.3 usec per loop

# "lesson_4_task_2_var_1.find_simple(40, 200)"
# 1000 loops, best of 5: 57.6 usec per loop

# cProfile.run('find_simple(10, 100)')
# 7 function calls in 0.000 seconds

# cProfile.run('find_simple(20, 100)')
# 7 function calls in 0.000 seconds

# cProfile.run('find_simple(40, 200)')
# 7 function calls in 0.000 seconds