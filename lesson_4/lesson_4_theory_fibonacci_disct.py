import cProfile

def test_fib(func):                             #Функция для теста основной функции
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]    #Тестовые данные
    for i, item in enumerate(list):
        assert item == func(i)                  #сравнение тестовых данных с результатом выполнения основной функции
        print(f'Test {i} OK')                   #вывол просто для наглядности

def fib_dict(n):  # сохраняем результаты вычислений в словарь
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)

test_fib(fib_dict)