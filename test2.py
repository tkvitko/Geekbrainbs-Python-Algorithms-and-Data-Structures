n = 2
result = []
while len(result) != 5:
    d = 2
    while n % d != 0:
        d += 1
    print(f'n = {n}')
    print(f'd = {d}')

    if d == n:
        result.append(d)
    n += 1

print(result)