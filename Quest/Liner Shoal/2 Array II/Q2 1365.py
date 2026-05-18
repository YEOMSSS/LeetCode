# -------------------------------
# Link : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-04
# Problem Number : 1365


# [Problem] How Many Numbers Are Smaller Than the Current Number

# 랜덤한 자연수로 이루어진 list nums가 들어온다.
# 어느 한 수가 자신이 아닌 다른 수에 비해 큰 횟수가 몇 회인지 각각 구해 list형태로 return하시오.


# [Intuition]

# 브루트포스로 다 비교해봐도 될 것 같은데.
# 어차피 자신이랑은 False잖아.

# 근데 힌트를 봤거든? 그냥 답을 알려주는 수준이네.
# 정렬하고 겹치는거 제일 앞 인덱스가 답이 되는거야...

from collections import defaultdict


def solve(nums: list[int]) -> list[int]:

    ##########

    result = [0] * len(nums)

    # dict에는 n이 등장하는 인덱스가 list로 저장된다.
    num_to_index = defaultdict(list)
    for i, num in enumerate(nums):
        num_to_index[num].append(i)

    # 겹치는 경우 첫 번째 n에 대해서만 처리한다.
    prev = None

    # 인덱스가 자신보다 작은 자연수들의 수가 된다.
    for c, n in enumerate(sorted(nums)):
        if prev == n:
            continue
        for i in num_to_index[n]:
            result[i] = c
        prev = n

    ##########

    return result


# [LeetCode]


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        return solve(nums)


# [Summary]

# 그냥 브루트포스로 풀면 쉬운데, 최적화가 가능한 좋은 문제.
# 최적화할때는 마냥 무지성으로만 할 순 없다.


# [Review]

# 이런 문제가 많은거같음. 그냥 막 풀어도 되긴 하는데.
# 풀 수 있는 훨씬 좋은 방법이 좀 많음.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
