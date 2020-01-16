import cProfile
import functools


def test_fib(func):  # Функция для теста основной функции
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Тестовые данные
    for i, item in enumerate(list):
        assert item == func(i)  # сравнение тестовых данных с результатом выполнения основной функции
        print(f'Test {i} OK')  # вывол просто для наглядности


@functools.lru_cache()  # декоратор
def fib(n):  # основная функция
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)  # считает Фибоначчи рекурсией

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
# 177/1    0.000    0.000    0.000    0.000 lesson_4_theory_fibonacci.py:9(fib)

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.010 seconds
# 21891/1    0.010    0.000    0.010    0.010 lesson_4_theory_fibonacci.py:9(fib)

# test_fib(fib)                                   #запуск теста для основной функции

# "lesson_4_theory_fibonacci.fib(10)"
# 1000 loops, best of 5: 27.5 usec per loop

# "lesson_4_theory_fibonacci.fib(20)"
# 1000 loops, best of 5: 3.69 msec per loop
