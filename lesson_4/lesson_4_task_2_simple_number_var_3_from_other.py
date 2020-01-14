def func(n):
    m = 3 * n  # задаем размер массива натуральных чисел
    print(m)
    prims = []  # массив для хранения простых чисел
    print(prims)
    #   i = 0
    while len(prims) < n:
        prims = []  # обнуляем массив для хранения простых чисел
        nums = list(range(m + 1))  # массив для хранения натуральных чисел
        print(nums)
        for i in nums:  # просеиваем nums
            if i > 1:
                for j in range(i + i, len(nums), i):
                    nums[j] = 0
        print(nums)
        print(prims)
        for i in nums:  # заполняем prims
            if i > 1:
                if len(prims) < n:
                    prims.append(i)
        print(prims)
        m = m * 2  # если nums закончился, а prims еще не наполнился, удваиваем размер nums и пробуем еще раз
    return prims[-1]  # последнее число в массиве и есть искомое

print(func(5))