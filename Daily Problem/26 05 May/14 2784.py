from typing import List, Optional

# -------------------------------
# Link : 0000000000000000000000
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-14
# Problem Number : https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

# -------------------------------

# [Problem] 배열이 좋은지 확인하기

# nums가 입력된다.
# 1~n을 모두 한 번씩 가지고 n을 하나 더 가지는 리스트인지 확인하시오.


# [Intuition]

# 확인할 건 3가지인가. 일단 정렬부터 하고.
# 길이 체크. 길이가 nums[-1] + 1이어야 한다.
# 최댓값 체크. nums[-1]이 길이 - 1이어야 한다.
# 값 체크. 각 값은 자신의 인덱스 + 1이어야 한다.

# 오, 근데 하고 보니 길이랑 최댓값 구하는 부등식이 똑같네?


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        N = len(nums)

        # 길이 체크
        if N != nums[-1] + 1:
            return False

        # 최댓값 체크(부등식이 길이체크와 동일)
        # if nums[-1] != N - 1:
        #     return False

        # 인덱스와 값 체크
        for i, v in enumerate(nums[:-1]):
            if i + 1 != v:
                return False

        return True


# -------------------------------

# [Summary]

# 일치하지 않는 경우를 빠르게 걸러주면 되는 문제.
# 정렬만 하면 쉽게 풀 수 있다.


# [Review]

# 부등식이 똑같네? 신기하네.
