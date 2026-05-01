# -------------------------------
# Link : https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-01
# Problem Number : Array I - Q1


# [Problem] Concatenation of Array

# 1K 이하 자연수로 이루어진 1K 이하 크기의 리스트 nums가 들어온다.
# nums와 nums를 붙여 만든 리스트를 return하시오.


# [Intuition]

# concatenate가 사슬 같이 있다라는 뜻의 단어였다.
# 그렇다면 이 문제도 이해가 되지.
# 그냥 붙이면 된다. extend를 사용하거나 +를 사용하면 될 듯.


def solve(nums: list[int]) -> list[int]:

    ##########

    # result = nums + nums
    result = nums
    result.extend(nums)

    ##########

    return result


# [LeetCode]


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return solve(nums)


# [Summary]

# 두 리스트를 더하는 간단한 문제.
# extend를 사용해도 좋다.


# [Review]

# 이런게 한 브론즈 5정도 되지 않을까?
# 음, 브론즈 3 정도 예상한다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
