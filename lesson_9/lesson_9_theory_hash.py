h_list = [None] * 26
print(h_list)

def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)

a = 'apricot'
my_append(a)

b = 'banana'
my_append(b)

c = 'apple'
my_append(c)        # хеш-коллизия

def my_index(value):    # простейшая хеш-функция
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') +1) * letter ** i

    return index % size

print(my_index(a))
print(my_index(b))
print(my_index(c))