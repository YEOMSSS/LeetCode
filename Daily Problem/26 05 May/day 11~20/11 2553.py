# -------------------------------
# Link : https://leetcode.com/problems/separate-the-digits-in-an-array/?envType=daily-question&envId=2026-05-11
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-11
# Problem Number : 2553

# -------------------------------

# [Problem] Separate the Digits in an Array

# 자연수로 이루어진 리스트가 들어온다.
# 각 자연수를 한 자리씩 나누어 모두 저장한 리스트를 반환하시오.


# [Intuition]

# 자연수를 ch로 바꿔서 한자리씩 int로 변경해서 append하면 빠르다.

# -------------------------------


def solve(nums: list[int]) -> list[int]:

    ##########

    res = []
    for n in nums:
        for ch in str(n):
            res.append(int(ch))

    ##########

    return res


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return solve(nums)


# -------------------------------

# [Summary]

# 그냥 사이트에서 풀어버렸다.


# [Review]

# 월요일이 easy인가?

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))
    print(solve(nums))
