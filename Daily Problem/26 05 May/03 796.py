# -------------------------------
# Link : https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2026-05-03
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-03
# Problem Number : 796


# [Problem] Rotate String

# string s와 goal이 들어온다.
# s의 가장 왼쪽 char를 가장 오른쪽으로 옮기는 동작을 반복해서
# goal을 만들 수 있는지 구하시오.


# [Intuition]

# rotate로 돌리는 게 제일 좋아 보인다.
# 하나 돌리고 goal이랑 비교하고를 반복하자.
# 최좌측이 최우측으로 이동하는 거니까, rotate(-1)이다.
# 사실 상관없긴함. 문자열의 길이는 100 이하이다.


from collections import deque


def solve(s: str, goal: str) -> bool:

    ##########

    string = deque(s)
    target = deque(goal)

    for _ in range(len(s)):
        if string == target:
            return True

        string.rotate(-1)

    ##########

    return False


# [LeetCode]


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return solve(s, goal)


# [Summary]

# rotate로 하나하나 돌려가며 찾으면 된다.
# 최대 100회여서 편하게 비교 가능.


# [Review]

# easy로 나오니까 또 진짜 쉽긴 하네.
# 난이도가 3개밖에 없어서 진짜 너무 헷갈린다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    s = input().rstrip()
    goal = input().rstrip()

    print(solve(s, goal))
