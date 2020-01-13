# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import cProfile

def find_mins(len):
    import random

    list = [random.randint(0, 10) for i in range(10)]

    min_1 = 10
    min_2 = 10

    for i in list:
        if i < min_1:
            min_1 = i
        elif i < min_2:
            min_2 = i
    return(min_1, min_2)

# "lesson_3_task_7_alt_1.find_mins(20)"
# 1000 loops, best of 5: 21.9 usec per loop

# "lesson_3_task_7_alt_1.find_mins(100)"
# 1000 loops, best of 5: 22.2 usec per loop

# "lesson_3_task_7_alt_1.find_mins(500)"
# 1000 loops, best of 5: 22.3 usec per loop

# cProfile.run('find_mins(20)')
# 3211 function calls (3149 primitive calls) in 0.033 seconds

# cProfile.run('find_mins(100)')
# 3213 function calls (3151 primitive calls) in 0.053 seconds

# cProfile.run('find_mins(500)')
# 3209 function calls (3147 primitive calls) in 0.034 seconds

# Этот способ работает быстрее и сложность меньше.
# Более того, скорость и сложность не зависят от длины массива.