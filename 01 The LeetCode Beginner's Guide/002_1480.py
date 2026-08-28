# -------------------------------

# Authored by : marigold2003
# Date : 2026-08-28
# Problem Number : 1480

# -------------------------------

# [Problem] Running Sum of 1d Array

# 배열이 주어진다. 누적합 배열을 만드시오.

# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import deque

# -------------------------------


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        acc = deque()
        acc.append(0)

        for n in nums:
            acc.append(n + acc[-1])

        acc.popleft()
        return list(acc)


# -------------------------------

# [Summary]

# 0을 생략해야 하는데, 덱으로 해봤다.


# [Review]

# 도파민 디톡스 중
