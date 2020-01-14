from collections import defaultdict

list_1 = [('cat', 1), ('dog', 5), ('cat', 1), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

d = defaultdict(set)
for k, v in list_1:
    d[k].add(v)
print(d)