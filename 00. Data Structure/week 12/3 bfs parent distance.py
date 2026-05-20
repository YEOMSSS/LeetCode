import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline


V, E = map(int, input().split())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    _from, _to = map(int, input().split())
    graph[_from].append(_to)
    graph[_to].append(_from)


from collections import deque


def bfs(start):
    queue = deque()
    Visited = [False] * (V + 1)
    Parent: list = [None] * (V + 1)
    Distance: list = [None] * (V + 1)

    queue.append(start)
    Visited[start] = True
    Parent[start] = -1
    Distance[start] = 0

    while queue:
        curr = queue.popleft()
        print(curr, end=" ")

        for nei in graph[curr]:
            if Visited[nei]:
                continue
            queue.append(nei)
            Visited[nei] = True
            Parent[nei] = curr
            Distance[nei] = Distance[curr] + 1

    print()
    print(Parent)
    print(Distance)


bfs(1)
