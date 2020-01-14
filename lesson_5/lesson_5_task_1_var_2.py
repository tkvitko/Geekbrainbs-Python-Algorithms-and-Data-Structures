from collections import namedtuple

"""""
Этот вариант написал только для того, чтобы поупражняться с namedtuple.
К сожалению, он не позволяет работать с динамическим количеством предприятий, 
т.к. как создавать переменные в цикле я пока не знаю.
"""""

props = ['name', 'q1_profit', 'q2_profit', 'q3_profit', 'q4_profit']

prod = namedtuple('prod', props)

prod_1 = prod('Intel', 10, 10, 10, 10)
prod_2 = prod('HP', 10, 20, 40, 30)
prod_3 = prod('IBM', 15, 25, 35, 45)

prod_1_sum = prod_1.q1_profit + prod_1.q2_profit + \
             prod_1.q3_profit + prod_1.q4_profit

prod_2_sum = prod_2.q1_profit + prod_2.q2_profit + \
             prod_2.q3_profit + prod_2.q4_profit

prod_3_sum = prod_3.q1_profit + prod_3.q2_profit + \
             prod_3.q3_profit + prod_3.q4_profit

avg_sum = (prod_1_sum + prod_2_sum + prod_3_sum)/3

sums_list = [prod_1_sum, prod_2_sum, prod_3_sum]
winners_list = []
loosers_list = []

for i in range(3):
    if sums_list[i] > avg_sum:
        winners_list.append()