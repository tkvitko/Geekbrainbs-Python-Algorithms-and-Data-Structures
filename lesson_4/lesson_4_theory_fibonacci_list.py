import cProfile


def test_fib(func):  # Функция для теста основной функции
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Тестовые данные
    for i, item in enumerate(list):
        assert item == func(i)  # сравнение тестовых данных с результатом выполнения основной функции
        print(f'Test {i} OK')  # вывол просто для наглядности


def fib_list(n):  # сохраняем результаты вычислений в список
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


test_fib(fib_list)
