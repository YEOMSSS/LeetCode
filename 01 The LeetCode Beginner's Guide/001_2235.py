import sys

input = sys.stdin.readline


# -------------------------------
# Link : https://leetcode.com/problems/add-two-integers/
# -------------------------------


# Authored by : marigold2003
# Date : 2026-04-30
# Problem Number : 2235


# [Problem] Add Two Integers

# 두 정수가 주어진다.
# 두 정수의 합을 반환하시오.


# [Intuition]

# num1과 num2를 그냥 더하면 될 것 같다.


def solve(num1: int, num2: int) -> int:

    ##########

    result = num1 + num2

    ##########

    return result


# [LeetCode]


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return solve(num1, num2)


# [Summary]

# 두 정수를 더해서 반환하는 문제.


# [Review]

# 리트코드를 시작해 보자. 반갑다, 반가워.

# -------------------------------
# -------------------------------


if __name__ == "__main__":

    # [Input]

    num1, num2 = map(int, input().split())
    print(solve(num1, num2))
