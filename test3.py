num1 = [2, 3, 4]
num2 = [5, 6, 7]

list = []

for j in num2:
    list_j = []
    for i in num1:
        local_comp = i * j
        list_j.append(local_comp)

    list.append(list_j)

#print(list)

# Добавляем нули справа для каждой строки
for i, item in enumerate(list):
    for j in range(i):
        item.insert(0, 0)



# Добавляем нули слева для каждоый строки
for i, item in enumerate(list):
    for j in range(len(num2) - i - 1):  #!!!!
        item.append(0)

print(list)

# Суммирование итоговых строк в столбик
sum_list = []
for j in range(5):
    print(f'j= {j}')
    sum_local = []
    for i in range(3):
        print(f'i= {i}')
        sum_local[i] += list[j][i]



print(sum_list)