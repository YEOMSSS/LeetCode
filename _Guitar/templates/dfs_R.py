V, E = map(int, input().split())
Graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    _from, _to = map(int, input().split())
    Graph[_from].append(_to)
    Graph[_to].append(_from)

visited = [False] * (V + 1)


def dfsR(curr):
    visited[curr] = True
    print(curr, end=" ")

    for nei in Graph[curr]:
        if visited[nei]:
            continue
        dfsR(nei)
