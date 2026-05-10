# -------------------------------
# Link : https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/?envType=daily-question&envId=2026-05-10
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-10
# Problem Number : 2770

# -------------------------------

# [Problem] Maximum Number of Jumps to Reach the Last Index

# 2*1G 이하의 target이 주어진다.
# 이동목표값 빼기 현재값 이 -target ~ target 사이의 값이면 이동이 가능하다.
# 이동은 오른쪽으로만 가능하며, 배열의 크기는 1K 이하이다.
# 최대 이동 횟수를 return하시오.


# [Intuition]

# 이동목표값과 현재값의 차가 target보다 작으면 된다는거지.
# 이동 가능한 모든 경로를 확인해봐야 한다.
# dfsR로 하나하나 접근해보자.

# [Approach]

# 1. 0번 인덱스부터 시작해서 1~N-1 인덱스와 판정 후 전부 재귀를 들어간다.
# 2. N-1 인덱스에 도착하면 0을 return하고 이전 단계로 가서 1을 더하며 처음으로 돌아간다.
# 3. 갱신된 카운트의 최댓값을 return한다.

# -------------------------------

from functools import cache

INF = 10**12


def solve(nums: list[int], target: int) -> int:

    ##########

    N = len(nums)

    # cache로 dp 날먹하기. 없으면 시간초과가 난다.
    @cache
    def dfsR(i: int):
        # 도달 시 종료
        if i == N - 1:
            return 0

        result = -1000

        # 이동 가능한 모든 칸을 방문해본다.
        for j in range(i + 1, N):
            if abs(nums[i] - nums[j]) <= target:
                # 최댓값을 갱신한다.
                result = max(result, dfsR(j) + 1)

        return result

    answer = dfsR(0)

    ##########

    return -1 if answer < 0 else answer


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:

        return solve(nums, target)


# -------------------------------

# [Summary]

# 재귀 dfs로 깊이 들어가서 탐색했다. 깊어 봤자 1K라서 가볍다.
# cache를 이용하니 아주 쉽게 효율성을 높일 수 있었다.


# [Review]

# cache 이거 개사기잖아?

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))
    target = int(input())

    print(solve(nums, target))
