import cProfile


def test_fib(func):  # Функция для теста основной функции
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Тестовые данные
    for i, item in enumerate(list):
        assert item == func(i)  # сравнение тестовых данных с результатом выполнения основной функции
        print(f'Test {i} OK')  # вывол просто для наглядности


def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


test_fib(fib_loop)
