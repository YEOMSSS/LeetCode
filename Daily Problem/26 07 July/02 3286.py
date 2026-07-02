# -------------------------------

# Authored by : marigold2003
# Date : 2026-07-02
# Problem Number : 3286

# -------------------------------

# [Problem] Find a Safe Walk Through a Grid

# 왼쪽 위에서 오른쪽 아래 칸으로 이동해야 한다.
# 상하좌우 이동이 가능하며, 1을 만나면 체력이 1 깎인다.
# 오른쪽 아래 칸에 체력을 1 이상 남겨두고 도착할 수 있는지 판단하시오.


# [Intuition]

# bfs 큐를 최소힙으로 다루면서 체력를 적게 사용한 녀석부터 없앤다.
# 체력을 소모하면서 나아갈지, 사용한 체력을 늘리면서 나아갈지 고민해보자.

# -------------------------------

# [LeetCode]

from typing import List, Optional
from heapq import heappop, heappush

# -------------------------------


class Solution:

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        M = len(grid)
        N = len(grid[0])

        def check(y, x):
            if y < 0 or y >= M:
                return False
            if x < 0 or x >= N:
                return False
            return True

        min_heap = []
        visited = [[False] * N for _ in range(M)]

        if grid[0][0] == 0:
            heappush(min_heap, [0, 0, 0])
        elif grid[0][0] == 1:
            heappush(min_heap, [1, 0, 0])
        visited[0][0] = True

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        while min_heap:
            hp, y, x = heappop(min_heap)
            if hp == health:
                continue
            if y == M - 1 and x == N - 1:
                return True

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]
                if not check(ny, nx):
                    continue
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                if grid[ny][nx] == 0:
                    heappush(min_heap, [hp, ny, nx])
                elif grid[ny][nx] == 1:
                    heappush(min_heap, [hp + 1, ny, nx])

        return False


# -------------------------------

# [Summary]

# 우선순위 큐를 이용한 bfs 문제이다.
# 더 적은 1을 지나서 도착한 걸 먼저 소모하면 된다.


# [Review]

# 우선순위큐를 bfs에 사용하니 편하구나.
# 자료구조시간에 배운걸 잘 써보자.
