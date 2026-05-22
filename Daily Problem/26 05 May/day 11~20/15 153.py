from typing import List, Optional

# -------------------------------
# Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=daily-question&envId=2026-05-15
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-15
# Problem Number : 153

# -------------------------------

# [Problem] 회전 정렬 배열에서 최소값 찾기

# 정렬된 리스트를 반 갈라 앞뒤를 바꿔 붙인 nums가 들어온다.
# log(n)의 시간복잡도로 min(nums)를 구해 return하시오.


# [Intuition]

# log면 이분탐색이다.
# 근데 완전 정렬된게 아니라서 내장함수는 못쓰고, 원리를 이용해야함.
# 목표는 nums[left] <= nums[right]가 되는 시작점을 찾는 것이다.

# mid가 right보다 크면 left를 키워야 하고
# mid가 right보다 작으면 mid를 right로 한다.

# 그러면 최종 left가 최솟값이 된다.

# 4 5 6 7 8 9 "1" 2 3
# 5 6 7 8 9 "1" 2 3 4
# 8 9 "1" 2 3 4 5 6 7


# -------------------------------
# [LeetCode]
# -------------------------------


def b_search(nums: list) -> int:
    left = 0
    right = len(nums) - 1

    # left == right가 되도록 한다.
    while left < right:
        mid = (left + right) // 2

        # mid가 right보다 크면 키워봐도 된다.
        if nums[mid] > nums[right]:
            left = mid + 1
        # mid가 right보다 작으면 mid가 right가 된다.
        else:
            right = mid
        print(mid)

    return nums[left]


from bisect import bisect_left


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return b_search(nums)

    def findMin2(self, nums: List[int]) -> int:
        # 와, 나... bisect 기능 겁나 많네.
        return nums[bisect_left(nums, True, key=lambda x: x <= nums[-1])]


# -------------------------------

# [Summary]

# 이분탐색의 원리를 이해하고 있다면 발상 자체는 쉽게 할 수 있다.
# 근데 늘 그렇듯 작은 인덱스 하나에서 큰 차이가 나타난다는거.


# [Review]

# 생각만큼 쉽지는 않았다고 하겠다.
