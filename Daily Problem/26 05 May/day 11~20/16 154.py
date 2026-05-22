from typing import List, Optional

# -------------------------------
# Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/?envType=daily-question&envId=2026-05-16
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-16
# Problem Number : 154

# -------------------------------

# [Problem] 회전 정렬 배열에서 최소값 찾기 II

# 정렬된 리스트를 반 갈라 앞뒤를 바꿔 붙인 nums가 들어온다.
# log(n)의 시간복잡도로 min(nums)를 구해 return하시오.
# nums의 요소는 중복될 수 있다.


# [Intuition]

# log면 이분탐색이다.
# 근데 완전 정렬된게 아니라서 내장함수는 못쓰고, 원리를 이용해야함.
# 목표는 nums[left] <= nums[right]가 되는 시작점을 찾는 것이다.

# mid가 right보다 크면 left를 키워야 하고
# mid가 right보다 작으면 mid를 right로 한다.

# 그러면 최종 left가 최솟값이 된다.

# 지금 이게 차이가 중복만인거지?
# 최솟값찾기1이랑 중복만 다른거잖아.

# 음, mid == right일 경우 어떤 동작을 해야 하는가?
# right -= 1은 안전하다. 이러면 최악의 경우 O(n)이 되는구나.

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
        elif nums[mid] < nums[right]:
            right = mid

        # 같으면 right만 한칸 줄여본다.
        else:
            right -= 1
        print(mid)

    return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return b_search(nums)


# -------------------------------

# [Summary]

# 이분탐색의 원리를 이해하고 있다면 발상 자체는 쉽게 할 수 있다.
# 근데 늘 그렇듯 작은 인덱스 하나에서 큰 차이가 나타난다는거.

# 중복이 가능한 경우는, if를 3가지로 나눠야 하는구나?
# mid보다 큰 경우, 작은 경우, 같은 경우로.
# 값이 mid와 동일한 경우도 처리해 줘야 한다는 거네. 안전한 걸 선택해야 한다.


# [Review]

# 한 줄 추가됐다고 논리가 이렇게 바뀌는구만.
