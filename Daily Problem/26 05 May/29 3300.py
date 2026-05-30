# -------------------------------
# Link : https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/?envType=daily-question&envId=2026-05-29
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-29
# Problem Number : 3300

# -------------------------------

# [Problem] Minimum Element After Replacement With Digit Sum

# 각 자릿수를 더해 만든 수 중에서 가장 작은 수를 return하시오.


# [Intuition]

# 야 이건 뭐.. 그냥 map(int, str(n))해서 sum치면 끝이지 뭐.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def minElement(self, nums: List[int]) -> int | float:
        min_num = float("inf")
        for n in nums:
            min_num = min(min_num, sum(map(int, str(n))))
        return min_num


# -------------------------------

# [Summary]

# 최솟값을 계속 갱신한다.


# [Review]

# 쉽고 편하게.
