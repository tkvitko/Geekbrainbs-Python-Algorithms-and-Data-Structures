# Написать алгоритм нахождения i-го по счёту простого числа без помощи алгоритма «Решето Эратосфена».
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import cProfile


def find_simple2(position, end):
    def create_simples():

        n = end
        all = [i for i in range(n)]
        simples = []
        not_simples = [0, 1]

        for i in all:
            for j in range(2, i - 1):
                if i % j == 0:
                    not_simples.append(i)

        simples = list(set(all) - set(not_simples))
        return simples

    lst = create_simples()
    number = lst[position]
    return number


print(find_simple2(5, 100))

# "lesson_4_task_2_var_2.find_simple2(10, 100)"
# 1000 loops, best of 5: 357 usec per loop

# "lesson_4_task_2_var_2.find_simple2(20, 100)"
# 1000 loops, best of 5: 329 usec per loop

# "lesson_4_task_2_var_2.find_simple2(40, 200)"
# 1000 loops, best of 5: 1.26 msec per loop

# cProfile.run('find_simple2(10, 100)')
# 282 function calls in 0.001 seconds

# cProfile.run('find_simple2(20, 100)')
# 282 function calls in 0.001 seconds

# cProfile.run('find_simple2(40, 200)')
# 695 function calls in 0.002 seconds
# 689    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# Измерение показали, что
# - метод "решета Эратосфена" быстрее и проще
