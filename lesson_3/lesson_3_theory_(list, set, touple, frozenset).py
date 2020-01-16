# Удаление элемента в списке во время его итерирования

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for i, item in enumerate(list_1):
    del item
print(list_1)
# Ни один элемент не удалился, т.к. del удаляет не элемент, а связь между переменной и объектом

for i, item in enumerate(list_2):
    list_2.remove(item)
print(list_2)

for i, item in enumerate(list_3):
    list_3.pop(i)
print(list_3)
# Элементы удалились через 1, т.к. после удаление список сдвигался влево

for i, item in enumerate(list_4[:]):
    list_4.remove(item)
print(list_4)
# Все элементы удалились, т.к. мы работали с КОПИЕЙ списка

# Задача про крестики-нолики
row = [''] * 3

board = [row] * 3  # в списке хранятся ССЫЛКИ на элементы
print(board)
board[0][0] = 'X'  # заполнились нулевые значения ВСЕХ строк
print(board)

board = [[''] * 3 for i in range(3)]  # так доска заполнилась отдельными строками
print(board)
board[0][0] = 'X'  # заполнилось нулевое значение ТОЛЬКО первой строки
print(board)

a = [1, 2, 3]
b = a
a = a + [5, 6, 7]  # При такой записи появляется НОВЫЙ список a, а b ссылается на старый
print(b)

a = [1, 2, 3]
b = a
a += [5, 6, 7]  # При такой записи меняется СТАРЫЙ список a, на который ссылается b
print(b)

t = ('one', 'two')
for i in t:
    print(i)

t = ('one')  # Без ЗАПЯТОЙ это строка, а не кортеж
for i in t:
    print(i)

t = ('one',)
for i in t:
    print(i)
