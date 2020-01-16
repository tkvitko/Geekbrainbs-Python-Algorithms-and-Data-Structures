# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import cProfile


def find_mins(len):
    import random

    min_item = 0
    max_item = 10

    list = [random.randint(min_item, max_item) for i in range(len)]

    def find_and_remove_min(list):
        min = 10
        pos_of_min = 0

        for i in list:
            if min > i:
                min = i
            pos_of_min = list.index(min)

        list.pop(pos_of_min)
        return min

    min1 = find_and_remove_min(list)
    min2 = find_and_remove_min(list)
    return (min1, min2)

#  "lesson_3_task_7_orig.find_mins(20)"
# 1000 loops, best of 5: 50.1 usec per loop

# "lesson_3_task_7_orig.find_mins(100)"
# 1000 loops, best of 5: 264 usec per loop

# "lesson_3_task_7_orig.find_mins(500)"
# 1000 loops, best of 5: 1.39 msec per loop

# cProfile.run('find_mins(20)')
# 3306 function calls (3244 primitive calls) in 0.060 seconds
#
# cProfile.run('find_mins(100)')
# 3898 function calls (3836 primitive calls) in 0.032 seconds
#
# cProfile.run('find_mins(500)')
# 6875 function calls (6813 primitive calls) in 0.034 seconds
