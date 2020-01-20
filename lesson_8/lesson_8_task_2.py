from collections import deque

# Граф хранится в матрице межности
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],  # 7 вместо 5?
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def deikstra(graph, start):
    length = len(graph)  # количество вершин (7)
    is_visited = [False] * length  # список посещенных вершин  [False, False, False, False, False, False, False]
    cost = [float('inf')] * length  # список расстояний [inf, inf, inf, inf, inf, inf, inf]
    parent = [-1] * length  # список родителей [-1, -1, -1, -1, -1, -1, -1]

    cost[start] = 0  # расстояние до 0 равно 0
    min_cost = 0  # минимальное расстояние 0
    list = [start]

    while min_cost < float('inf'):  # пока минимальное расстояние меньше бесконечности

        is_visited[start] = True  # стартовую вершину делаем посещенной

        for i, vertex in enumerate(
                graph[start]):  # мы на стартовой вершине, идем по ее связям (i - след вершина, vertex - расст до нее
            if vertex != 0 and not is_visited[i]:  # для всех непосещенных потомков

                if cost[i] > vertex + cost[
                    start]:  # если сохраненное ранее расстояние до потомка > расст до потомка + расст до текущей
                    cost[i] = vertex + cost[start]  # расстояние до потока = расст до потока + расст до текущей

                    parent[i] = start  # родителем потомка становится текущая стартовая вершина

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = [[] for i in range(length)]
    for i in range(length):
        if is_visited[i] == True:
            ways[i].append(i)
            j = i
            while parent[j] != -1:
                ways[i].append(parent[j])
                j = parent[j]
            ways[i].reverse()

    return cost, ways


s = int(input('Откуда '))
cost, ways = deikstra(g, s)
print(cost)
print(*ways, sep='\n')
