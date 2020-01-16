# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import ChainMap

number = int(input('Количество предприятий для анализа: '))

prod_list = []
profit_q1_list = []
profit_q2_list = []
profit_q3_list = []
profit_q4_list = []

for i in range(1, number + 1):
    prod_list.append(input(f'Название предприятия {i}: '))
    profit_q1_list.append(int(input(f'Доход за 1 квартал на предприятии {i}: ')))
    profit_q2_list.append(int(input(f'Доход за 2 квартал на предприятии {i}: ')))
    profit_q3_list.append(int(input(f'Доход за 3 квартал на предприятии {i}: ')))
    profit_q4_list.append(int(input(f'Доход за 4 квартал на предприятии {i}: ')))

prod_map = ChainMap()
for i in range(number):
    prod_map = prod_map.new_child({'name': prod_list[i],
                                   'q1': profit_q1_list[i], 'q2': profit_q2_list[i],
                                   'q3': profit_q3_list[i], 'q4': profit_q4_list[i]})

print(prod_map)

"""
Как использовать ChainMap в дальнейших рассчетах, не придумал.
Она не позволяет обратиться к конкретному элементу конкретного словаря; а их количество мы не знаем.
"""

year_profits = []
for i in range(number):
    year_profit = profit_q1_list[i] + profit_q2_list[i] + profit_q3_list[i] + profit_q4_list[i]
    year_profits.append(year_profit)
print(f'Годовые доходы {number} предприятий: {year_profits}')


def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


avg_sum_year = ((list_sum(profit_q1_list) + list_sum(profit_q2_list) +
                 list_sum(profit_q3_list) + list_sum(profit_q4_list))) / number

print(f'Средний доход за год: {avg_sum_year}')

list_overs = []
list_aboves = []

for i in range(len(year_profits)):
    if year_profits[i] > avg_sum_year:
        list_overs.append(prod_list[i])
    else:
        list_aboves.append(prod_list[i])

print(f'Прибыль выше среднего у предприятий {list_overs}')
print(f'Прибыль ниже среднего у предприятий {list_aboves}')
