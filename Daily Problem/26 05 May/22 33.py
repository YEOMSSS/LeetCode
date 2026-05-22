# -------------------------------
# Link : https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/2009942756/?envType=daily-question&envId=2026-05-22
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-22
# Problem Number : 33

# -------------------------------

# [Problem] Search in Rotated Sorted Array

# 회전된 정렬 배열에서 이분탐색을 이용해 원하는 원소를 찾아내시오.


# [Intuition]

# 이분탐색같음.
# 153번, 154번이랑 연계되는 내용으로 보인다.
# 중복 원소가 없다는 점에서 153번이랑 이어지는 것으로 추정.
# 최솟값을 찾는 건 둘의 관계가 바뀌는 부분으로 쉽게 찾을 수 있었지만, 검색은?


# [Approach]

# 1. bisect_left(nums, True, lambda x: x<= nums[-1])로 정렬된 배열의 시작인덱스를 찾는다.
# 2. mid에만 시작인덱스만큼 더해 일반적인 이분탐색을 진행하듯 한다.


# -------------------------------

# [LeetCode]

from typing import List, Optional
from bisect import bisect_left

# -------------------------------


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # True가 나오기 시작하는 순간을 반환한다.
        # nums[-1]보다 x가 작은 순간의 인덱스를 찾는다.
        rot = bisect_left(nums, True, key=lambda x: x <= nums[-1])

        # 일반적인 정렬 배열처럼 이분탐색을 진행하되,
        left = 0
        right = n - 1

        # 구한 mid에 rot만큼 더해서 인덱스를 지정한다.
        while left <= right:
            mid = (left + right) // 2
            real = (mid + rot) % n

            # 탐색 성공 시 반환한다.
            if nums[real] == target:
                return real

            # 작으면 왼쪽을 키우고
            if nums[real] < target:
                left = mid + 1
            # 크면 오른쪽을 줄이는 전형적인 이분탐색
            else:
                right = mid - 1

        # 탐색 실패.
        return -1


# -------------------------------

# [Summary]

# bisect_left에 다양한 기능이 있구나.
# 시작인덱스를 찾아내면 그걸 mid에 더해서 정렬된 셈 칠 수 있다.
# 또 좋은 거 하나 알아가는구만.


# [Review]

# 대가리 잘 굴려야 하네. 새로운 유형이 많다.
# 이런 게 웰노운이 될때까지 수련이 필요하겠어.
