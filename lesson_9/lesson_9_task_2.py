# 2. Закодируйте любую строку по алгоритму Хаффмана.
# Сам с заданием не справился, нашел реализацию в Internet и подробно разобрал.
# Вывел несколько ключевых мест в результат, разбирая работу алгоритма
# Комментарии автора сохранены

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, acc):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        # потомков у листа нет, по этому для значения мы запишем построенный код для данного символа
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"


def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
    h = []  # инициализируем очередь с приоритетами
    for ch, freq in Counter(s).items():  # постоим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    print(f'Список символов с весом: {Counter(s)}')
    heapq.heapify(h)  # построим очередь с приоритетами
    count = len(h)  # инициализируем значение счетчика длиной очереди
    while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # добавим новый внутренний узел у которого
        # потомки left и right соответственно
        count += 1  # инкрементируем значение счетчика при добавлении нового элемента дерева
    code = {}  # инициализируем словарь кодов символов
    print(f'Куча, представляющая дерево: {h}')
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = h  # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
    return code  # возвращаем словарь символов и соответствующих им кодов


s = input('Введите строку для кодирования: ')  # читаем строку длиной  до 10**4
code = huffman_encode(s)  # кодируем строку
encoded = ' '.join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
# в соответствующий код и конкатенируем результат
#    print(len(code), len(encoded))  # выведем число символов и длину закодированной строки
for ch in sorted(code):  # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
    print(f'{ch}: {code[ch]}')  # выведем символ и соответствующий ему код
print(f'Закодированная строка: {encoded}')  # выведем закодированную строку