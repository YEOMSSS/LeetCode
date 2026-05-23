# -------------------------------
# Link : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2026-05-23
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-23
# Problem Number : 1752

# -------------------------------

# [Problem] Check if Array Is Sorted and Rotated

# 정수 배열 nums가 회전된 비내림차순 배열인지 검사하시오.
# 값은 중복되게 들어있을 수 있다.
# 값은 1~100, 배열의 크기도 최대 100이다.


# [Intuition]

# 중복값도 들어갈 수 있네? 이거 계속 이어지는 시리즈구만?
# bisect True가 작동하는지 안하는지를 확인하면 된다.
# 뭐 인덱스만 확인하고 거기부터 정렬이 되어있는지 검사해도 좋고.
# 시간제한이 없어 편하게 푸는 문제다.

# bisect_left(nums, True, key=lambda x: x <= nums[-1])
# 라고 생각했는데~ 이걸로는 2 1 3 4 를 못 걸러내는구나.
# 그냥 다 확인하자고. 앞에서부터 시작해서 증가하거나 같은지 확인하고
# 감소하는 순간이 한번 이라면 통과인거지. [-1] -> [0]도 검사해야 한다.


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def check(self, nums: List[int]) -> bool:

        # 감소 기회 1회 사용 시 켜짐
        flag = False

        prev = 0
        for curr in nums:
            if prev > curr:
                if flag:
                    return False
                flag = True
            prev = curr

        # 한바퀴 도는 부분 검사
        if nums[-1] > nums[0]:
            if flag:
                return False
            # flag = True

        return True


# -------------------------------

# [Summary]

# 이전 값과 현재 값을 비교하는 것만으로도 간단하게 해결 가능.


# [Review]

# 괜히 최근에 회전배열에서 bisect 돌리는걸 배워가지고
# 써볼려다가 오히려 조졌네.
# 가장 단순하고 쉬운 방법이 가장 효율적인 풀이일 가능성이 높다.
