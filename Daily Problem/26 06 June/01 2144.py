# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-01
# Problem Number : 2144

# -------------------------------

# [Problem] Minimum Cost of Buying Candies With Discount

# 사탕을 두 개 사면 그 둘보다 다 작은 사탕 하나가 꽁짜다.
# 가장 싸게 모든 사탕을 사는 가격을 구하시오.


# [Intuition]

# 무조건 그리디임. 제일비싼거 두개고르고 그다음비싼거 골라야하나? 맞음.
# 비내림차정렬해서 두개넣고하나빼고 반복하면 됨. 사탕도 100개밖에 안되네


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        took = 0
        res = 0
        for i in range(n - 1, -1, -1):
            if took == 2:
                took = 0
                continue
            res += cost[i]
            took += 1

        return res


# -------------------------------

# [Summary]

# 간단하게 그리디임을 확인할 수 있었다.
# 왜냐? 최대한 비싼걸 무료로 가져가야하니까.


# [Review]

# 이지, 가 좋아. 이, 지가 좋아.
