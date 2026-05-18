# -------------------------------
# Link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-18
# Problem Number : 448

# -------------------------------

# [Problem] 배열에서 사라진 모든 숫자 찾기

# range(1, N+1)의 원소 중 길이 N인 nums에 포함되지 않는 원소를 리스트로 출력하시오.


# [Intuition]

# set으로 만들어서 차집합 구하면 될 듯?

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = set(range(1, len(nums) + 1))

        return list(check - set(nums))


# -------------------------------

# [Summary]

# 간단하게 차집합을 이용해서 풀었다.


# [Review]

# 추가 도전: 추가 공간 없이 O(n) 시간 복잡도로 해결할 수 있나요?
# 반환된 리스트는 추가 공간으로 간주하지 않을 수 있습니다.
