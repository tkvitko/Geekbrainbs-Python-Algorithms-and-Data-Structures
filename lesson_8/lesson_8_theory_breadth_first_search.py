from collections import deque

# Граф хранится в матрице межности
g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def bsf(graph, start, finish):
    # Граф; вершина, откуда надо выйти; вершина, в которую надо прийти

    parent = [None for i in range(len(graph))]      # храним родителя вершины
    is_visited = [False for i in range(len(graph))] # храним состояние вершины - побывав, True

    deq = deque([start])  # очередь, вначало котороый поместили старт
    is_visited[start] = True

    while len(deq) > 0: # пока очередь не пустая
        current = deq.pop() # забираем крайнее значение из очереди
        if current == finish:
            return parent
            break

        for i, vertex in enumerate(graph[current]):     # проверяем все вершины, связанные с текущей
            if vertex == 1 and not is_visited[i]:       # если можем перейти из текущей вершины в i-тую, и в i-той еще не были
                is_visited[i] = True
                parent[i] = current             # в список parent указываем, из какой вершины мы пришли
                deq.appendleft(i)               # добавляем в начало очереди i-тую вершину

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'Кратчайший путь {list(way)} длинною в {cost}'

s = int(input('Откуда '))
f = int(input('Куда '))
print(bsf(g, s, f))