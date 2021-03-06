# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# # Примечание. Решите задачу при помощи построения графа.

N = int(input('Введите количество друзей: '))

graph = []

# Построение графа
for i in range(N):
    for j in range(N):
        if i != j:  # сам себе руку не пожимал
            graph.append([i, j])

print(f'Список неуникальных рукопожатий: {graph}')

# Отфильтруем взаимные рукопожатия
result = []
for item in graph:
    if item[0] > item[1]:
        item[0], item[1] = item[1], item[0]  # упорядочим номера внутри каждой пары
    if result.count(item) == 0:
        result.append(item)  # заполним новый список уникальными парами

print(f'Список уникальных рукопожатий: {result}')
print(f'Количество рукопожатий: {len(result)}')
