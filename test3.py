num1 = [2, 3, 4]
num2 = [5, 6]

dif = abs(len(num1) - len(num2))
if dif:
    if len(num1) < len(num2):
        for i in range(dif):
            num1.insert(0, 0)
    else:
        for i in range(dif):
            num2.insert(0, 0)

print(num1, num2)

