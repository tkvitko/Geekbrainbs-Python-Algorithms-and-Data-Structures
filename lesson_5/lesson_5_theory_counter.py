from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats = 4, dogs = 5)

print (a, b, c, d, sep = '\n')

b['z'] = 0
print(b)
print(list(b.elements()))
print(b.most_common(3))

g = Counter(a=4, b=6)
f = Counter(a=1, b=2)
g.subtract(f)
print(g)
print(set(g))
print(dict(g))

g.clear()
print(g)

x = Counter(a=3, b=1, c=2, d=4)
y = Counter(a=1, b=2, c=3)
print(x + y)
print(x - y)
print(x & y)
print(x | y)