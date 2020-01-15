list = [[10, 15, 20, 0, 0], [0, 12, 18, 24, 0], [0, 0, 14, 21, 28]]

sum = []

sum = [list[0][0] + list[1][0] + list[2][0], list[0][1] + list[1][1] + list[2][1], list[0][2] + list[1][2] + list[2][2]]

sum_items = list[0][0] + list[1][0] + list[2][0]

sum_items = 0
for j in range(0, 2):
    sum_items += list[j][0]