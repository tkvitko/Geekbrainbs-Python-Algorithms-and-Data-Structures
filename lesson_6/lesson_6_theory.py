import sys

a = 42
print(bin(a))
print(oct(a))
print(hex(a))

z = int('z', base=36)
print(z)

print(sys.version)
print(sys.platform)

list = [i for i in range(10)]

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}), size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):  # объект итерируемый
        if hasattr(x, 'items'): # объект словарь
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):    # объект не строка
            for xx in x:
                show_size(xx, level + 1)

show_size(5)
show_size(3.456)
show_size('Hello')
show_size(list)     # список - изменяемый

print('*' * 50)
t = tuple(list)
show_size(t)        # кортеж - неизменяемый (занимает меньше памяти)

print('*' * 50)
s = set(list)
show_size(s)        # множетво - изменяемое из уникальных (занимает много места, но поиск по нему быстрее)

print('*' * 50)
d = {str(i): i for i in range(10)}
print(d)
show_size(d)        # словарь занимает меньше, чем множество