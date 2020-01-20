# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def build_graph(number):
    # Магическая функция, которая строит граф
    graph = []
    list = []

    # создаем "универсальный" список (пока с избыточными значениями)
    for i in range(number):
        list.append(str(i))

    # создаем словарь для графа, пока из избыточных списков
    graph = {str(a): list[:] for a in range(number)}

    # удаляем из списков избыточные значения
    for key, value in graph.items():
        for j in value:
            if j == key:
                value.remove(j)

    return graph

graph = build_graph(5)
print(graph)

def dfs(graph, start, visited=None):
    # множество для хранения посещенных вершин
    if visited is None:
        visited = set()
    visited.add(start)

    # убираем те вершины, что уже посетили
    for i in visited:
        if graph[start].count(i) > 0:
            graph[start].remove(i)

    # применяем функцию рекурсивно для тех вершин, что остались
    for next in graph[start]:
        dfs(graph, next, visited)
    return visited

print(dfs(graph, '0'))

