# -------------------------------
# Link : https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-04
# Problem Number : 645


# [Problem] Set Mismatch

# 자연수 배열 nums가 주어진다.
# nums는 1~n이 무작위 순서로 들어있는 list에서 숫자 하나가 중복되게 오류가 난 상태의 list이다.
# 중복된 숫자와 빠진 숫자를 배열 형태로 return하시오.

# 2<= len(nums) <= 10K, nums[i] <= 10K

# [Intuition]

# 중복된 원소는 Counter에서 most_common으로 뽑아내면 될 거고.
# 없는 원소는 set(range(1, n+1))에서 nums를 차집합하면 구할 수 있을 듯.

from collections import Counter


def solve(nums: list[int]) -> list[int]:

    ##########

    counter = Counter(nums)
    dup = counter.most_common(1)[0][0]

    numsSet = set(nums)
    res = set(range(1, len(nums) + 1)) - numsSet

    ##########

    return [dup, res.pop()]


# [Intuition]

# 에러합에서 set()합을 빼면 중복된 값이 나온다.
# range합에서 set()합을 빼면 없는 값이 나온다.


def solve2(nums: list[int]) -> list[int]:

    ##########

    n = len(nums)
    real_sum = n * (n + 1) // 2
    error_sum = sum(nums)
    set_sum = sum(set(nums))
    return [error_sum - set_sum, real_sum - set_sum]

    ##########


# [LeetCode]


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:

        return solve(nums)


# [Summary]

# 차집합을 이용해서 빠진 수를 찾아내기.
# Counter를 이용해서 중복된 수를 찾아내기.


# [Review]

# 이따위로 풀었지만 사실 배열 하나 만들어서 쌓아도 상관없다는거.
# False로 시작해서 있으면 True로 바꾸고, True인애가 또있으면 걔가 중복.
# 마지막까지 해서 혼자 False인 애가 빠진 애.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
