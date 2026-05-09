# -------------------------------
# Link : https://leetcode.com/problems/cyclically-rotating-a-grid/description/?envType=daily-question&envId=2026-05-09
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-08
# Problem Number : 1914

# -------------------------------

# [Problem] Cyclically Rotating a Grid

# 짝수인 m과 n이 있다. m*n(<=50) board가 들어온다.
# 테두리를 한 단계로 묶어 시계 반대방향으로 한칸씩 이동시킨다.
# 이동을 k회 한 결과를 return하시오. k는 매우 커질 수 있다.


# [Intuition]

# 새 배열 하나 만들어서 변을 하나씩 밀어서 저장하면 될 듯.
# k는 대충 테두리 칸 개수로 mod해서 쓰면 될 듯.

# 아니면, deque에 몰아넣고 확 rotate 시켜서 다시 집어넣어버려??
# 새 배열도 필요 없겠네.

# [Approach]

# 1. 테두리를 꺼내서 deque에 넣고 칸수로 mod한만큼 -rotate시킨다.
# 2. 꺼낸 순서대로 다시 집어넣는다.

# -------------------------------


from collections import deque


def solve(grid: list[list[int]], k: int) -> list[list[int]]:

    ##########

    M = len(grid)
    N = len(grid[0])

    for i in range(min(M, N) // 2):
        dq = deque()

        for c in range(i, N - i):
            dq.append(grid[i][c])

        for r in range(i + 1, M - i):
            dq.append(grid[r][N - i - 1])

        for c in range(N - i - 2, i - 1, -1):
            dq.append(grid[M - i - 1][c])

        for r in range(M - i - 2, i, -1):
            dq.append(grid[r][i])

        tmp = k % (((M - i * 2 - 1) + (N - i * 2 - 1)) * 2)
        dq.rotate(-tmp)

        it = iter(dq)

        for c in range(i, N - i):
            grid[i][c] = next(it)

        for r in range(i + 1, M - i):
            grid[r][N - i - 1] = next(it)

        for c in range(N - i - 2, i - 1, -1):
            grid[M - i - 1][c] = next(it)

        for r in range(M - i - 2, i, -1):
            grid[r][i] = next(it)

    ##########

    return grid


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        return solve(grid, k)


# -------------------------------

# [Summary]

# 원하는 묶음으로 꺼내서 rotate로 돌리기
# 다시 원래 있던 순서대로 집어넣기


# [Review]

# 뭔가 deque를 쓸 일이 많네?
# 그리고 인덱스를 세밀하게 관리하는게 좀 많은 거 같음.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    k = int(input())

    print(solve(grid, k))
