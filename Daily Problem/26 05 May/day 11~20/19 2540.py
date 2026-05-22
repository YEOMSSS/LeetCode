# -------------------------------
# Link : https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2026-05-19
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-19
# Problem Number : 2540

# -------------------------------

# [Problem] Minimum Common Value

# 비내림차순으로 정렬된 두 리스트가 들어온다.
# 두 배열의 교집합에서 최솟값을 반환하시오.
# 교집합이 없다면 -1을 반환한다.


# [Intuition]

# 둘 다 set치고 &로 교집합내서 min을 반환하자.
# 비내림차순임을 이용해 투포인터를 써도 될 듯.


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        temp = set(nums1) & set(nums2)
        return min(temp) if temp else -1


# -------------------------------

# [Summary]

# 대충 set으로 교집합 내서 min을 반환했다.


# [Review]

# easy 걸리면 기분이가 좋아요.
