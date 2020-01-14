from collections import defaultdict

a = defaultdict()
print(a)

s = 'fwefwafafdasfasfdasfa'
b = defaultdict(int)
print(b)
for i in s:
    b[i] += 1

print(b)


list_1 = [('cat', 1), ('dog', 5), ('cat', 1), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

d = defaultdict(set)
for k, v in list_1:
    d[k].add(v)
print(d)

f = defaultdict(lambda: 'unknown')
print(f)
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])