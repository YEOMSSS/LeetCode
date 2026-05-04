# -------------------------------
# Link : https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-03
# Problem Number : 1470


# [Problem] Shuffle the Array

# n(<=500) *2 길이의 list가 들어온다.
# [x1, x2, ..., xn, y1, y2, ..., yn] 형태를
# [x1, y1, x2, y2, ..., xn, yn] 형태로 반환하시오.


# [Intuition]

# for문으로 인덱스 조절하면 된다.
# 정답용 리스트 하나 만들어서 i, n+i를 차례로 append하면 될 듯.


def solve(nums: list[int], n: int) -> list[int]:

    ##########

    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])

    ##########

    return result


# [LeetCode]


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:

        return solve(nums, n)


# [Summary]

# 투 포인터 개념으로 기존 리스트 shuffle하기.
# for문과 index를 사용해서 간단히 해결할 수 있다.


# [Review]

# 퀘스트는 빨리빨리 밀어야겠다. 확실히 초반 난이도는 브론즈 하위에 가깝다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))
    n = int(input())

    print(solve(nums, n))
