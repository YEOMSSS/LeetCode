import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline


V, E = map(int, input().split())
myMap = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    _from, _to = map(int, input().split())
    myMap[_from].append(_to)
    myMap[_to].append(_from)

visited = [False] * (V + 1)


def dfsR(here):
    visited[here] = True
    print(here, end=" ")

    for nxt in myMap[here]:
        if not visited[nxt]:
            dfsR(nxt)


dfsR(1)
