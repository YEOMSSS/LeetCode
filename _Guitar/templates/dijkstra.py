from heapq import heappop, heappush


def dijkstra(graph, start, end=None):
    n = len(graph)

    min_heap = [(0, start)]
    seen = set()
    d = [float("inf")] * n
    d[start] = 0

    while min_heap:
        _, curr = heappop(min_heap)
        if curr in seen:
            continue
        seen.add(curr)
        for child, w in graph[curr]:
            if d[curr] + w < d[child]:
                d[child] = d[curr] + w
                heappush(min_heap, (d[child], child))

    if end:
        return d[end]

    return d


graph = {
    0: [(1, 1), (2, 4)],  # (node, weight)
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: [],
}

print(dijkstra(graph, 1))  # node 1 to all nodes
print(dijkstra(graph, 1, 2))  # node 1 to 4
