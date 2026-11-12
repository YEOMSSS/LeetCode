import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------

N = int(input())

# 파이썬의 꽃은 딕셔너리인가?
graph = {}

for _ in range(N):
    _from, _to, weight = input().split()
    weight = int(weight)

    if _from not in graph:
        graph[_from] = []
    graph[_from].append((_to, weight))

    if _to not in graph:
        graph[_to] = []
    graph[_to].append((_from, weight))

print(graph)
