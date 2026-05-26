# -------------------------------
# Link : https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-26
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-26
# Problem Number : 3120

# -------------------------------

# [Problem] Count the Number of Special Characters I

# 대문자와 소문자로 이뤄진 string이 주어질 때,
# 대문자와 소문자가 모두 등장하는 알파벳의 종류의 수를 return하시오.


# [Intuition]

# 배열 두개 대문자 소문자로 각각 만들어서 저장하자.
# ord 써서 인덱스 판정하면 될 듯.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        U = [False] * 26
        L = [False] * 26

        ordA = ord("A")
        orda = ord("a")
        for ch in word:
            ordch = ord(ch)
            if ordch - ordA < 26:
                if not U[ordch - ordA]:
                    U[ordch - ordA] = True
            else:
                if not L[ordch - orda]:
                    L[ordch - orda] = True

        result = 0
        for i in range(26):
            if U[i] and L[i]:
                result += 1

        return result


# -------------------------------

# [Summary]

# ord 사용하기


# [Review]

# easy가 나오면 기분이가 좋아요.
