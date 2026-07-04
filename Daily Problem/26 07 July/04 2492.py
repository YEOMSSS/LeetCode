# -------------------------------

# Authored by : marigold2003
# Date : 2026-07-04
# Problem Number : 2492

# -------------------------------

# [Problem] Minimum Score of a Path Between Two Cities

# 그래프에 1~n의 번호를 가진 정점이 있고, 1에서 시작해서 n에 도착한다.
# 가는 길에 지나갈 수 있는 가장 짧은 도로의 길이를 반환하시오.


# [Intuition]

# 이어져있기만 하면 다 갈 수 있는거잖아? 섬 찾는 문제다.

# 출발지와 도착지가 포함된 섬에서 가장 작은 가중치를 찾으면 된다. bfs로 할까.
# 어차피 출발지와 도착지는 이어져있으니 s출발지기준으로 bfs돌려서
# 제일 가중치가 작은 걸 찾으면 되겠네.

# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import deque

# -------------------------------


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = [[] for _ in range(n + 1)]
        dist = [set() for _ in range(n + 1)]
        for a, b, d in roads:
            graph[a].append(b)
            graph[b].append(a)
            dist[a].add(d)

        queue = deque()
        islands = set()

        queue.append(1)
        islands.add(1)

        while queue:
            curr = queue.popleft()

            for nei in graph[curr]:
                if nei in islands:
                    continue
                islands.add(nei)
                queue.append(nei)

        result = set()
        for i in islands:
            result.update(dist[i])

        return min(result)


# -------------------------------

# [Summary]

# 간단한 그래프 순회 문제다.


# [Review]

# 순회해서 방문정점을 찾고, 거기서 min으로 제일 짧은 걸 찾았다.
# 쉽게쉽게 풀었다. 문제를 내가 아는 쉬운 유형으로 변형할 수 있었다.
