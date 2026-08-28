# -------------------------------

# Authored by : marigold2003
# Date : 2026-08-28
# Problem Number : 1672

# -------------------------------

# [Problem] Richest Customer Wealth

# accounts[i][j]는 i​​​​​​​​​​​th​​​​ 고객이 j​​​​​​​​​​​th​​​​ 은행에 가진 돈의 양입니다.
# 가장 부유한 고객이 가진 재산을 반환하세요.


# [Intuition]

# 그니까 한줄에 그 고객이 가진 돈이 은행에 나눠져 있다는거잖아.
# sum쳐서 max구하면 되는 문제

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        return max(map(sum, accounts))


# -------------------------------

# [Summary]

# map 쓰기


# [Review]

# map을 써? 너 아직 기억을 잃지는 않았구나?
# 그래도 사람새끼긴 하네?
