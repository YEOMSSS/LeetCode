# -------------------------------
# Link : https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-03
# Problem Number : 485


# [Problem] Max Consecutive Ones

# length가 10K 이하인 binary list nums가 주어진다.
# 1이 가장 많이 연속되는 횟수를 count해 return하시오.


# [Intuition]

# groupby를 사용할 수 있는 문제 같다.

from itertools import groupby


def solve1(nums: list[int]) -> int:

    ##########

    result = 0

    for n, group in groupby(nums):
        if not n:
            continue
        result = max(result, len(list(group)))

    ##########

    return result


def solve(nums: list[int]) -> int:

    ##########

    result = 0

    count = 0
    for n in nums:
        if n:
            count += 1
        else:
            result = max(result, count)
            count = 0

    result = max(result, count)

    ##########

    return result


# [LeetCode]


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        return solve(nums)


# [Summary]

# 그냥 인덱스로 세는 게 더 빨랐을까?


# [Review]

# groupby 말고, 아예 숫자까지 세 주는 함수는 없나?
# 음, Counter는 연속성이 없으니 안되겠네. 이게 최대다.

# 그냥 index counting하는게 베스트. 크기가 작으니까.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
