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

print(func1(5))