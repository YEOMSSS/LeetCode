from typing import List, Optional

# -------------------------------
# Link : https://leetcode.com/problems/minimum-moves-to-make-array-complementary/?envType=daily-question&envId=2026-05-13
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-13
# Problem Number : 1674

# -------------------------------

# [Problem] Minimum Moves to Make Array Complementary

# 정수 리스트 nums가 주어진다.
# 모든 인덱스 i에서 nums[i] + nums[n - 1 - i]가 일치하면
# 보완적이라고 표현한다.
# nums를 보완적으로 만들기 위해 필요한 최소 이동 횟수를 반환하시오.


# [Intuition]

# 이게 반 접었을 때 더해가지고 다 똑같이 나와야 된다는 거 같은데.
# 배열 길이가 100K? 50K번 확인은 어렵지 않을 것 같은데.
# 합 50K개 구해서 Counter로 개수 세가지고 common뽑으면 되는거아니냐?
# n//2 - 최빈횟수 하면 답 나오는거같은디.

# 어, limit는 어떡하지?
# 아 씨, 하나하나 다해봐야하는건가.
# 그래, 이렇게 단순할 리가 없지.
# limit도 최대 100K니까, 1~limit*2까지 합을 다 해본단 마인드로 가볼까.
# 그럼 이분탐색밖에 답이 없네.

# 각 쌍에 대해서 연산은 0회 1회 2회로 나눠진다.
# 이미 합이 c면 안해도 되고, 하나만 바꿔서 되는 경우도 있지.
# 근데 만약 c보다 큰 값이 있으면 걔는 무조건 바꿔야 한다.

# 작은게 바뀌는 경우는 c보다 크면 무조건 바꿔야 하고,
# 큰게 바뀌는 경우는 c-limit보다 작으면 무조건 바꿔야 한다.

# 경우는 세가지다.
# 둘다바꿔야하거나, 하나만바꾸면되거나, 안바꿔도되거나.
# 둘다 limit보다 크면 둘다 바꿔야 하고
# 둘다 목표합-limit보다 작으면 둘다 바꿔야 한다.

# [Approach]
# 1. 합의 개수를 counter로 세고, 작은값과 큰값을 분리해 list로 저장한다.
# 2. 작은값 리스트와 큰값 리스트를 각각 비내림차순 정렬해 bisect_left를 준비한다.
# 3. 합이 될 수 있는 모든 범위를 검사한다. 2*1 ~ 2*limit
# 4. 모든 쌍에서 변경이 1회 있다고 가정하자.
#    작은 값에서 합보다 큰 애들은 추가로 변경해야 한다.
#    큰 값에서 limit-합보다 작은 애들은 추가로 변경해야 한다.
#    바꾸지 않아도 합이 일치하는 경우를 counter에서 가져와서 빼 준다.
# 5. 모든 합의 경우에 대해 최소변경횟수로 갱신한다.


# -------------------------------
# [LeetCode]
# -------------------------------

from collections import Counter
from bisect import bisect_left


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        N = len(nums)

        mins = []
        maxs = []
        counter = Counter()

        for i in range(N >> 1):
            a = nums[i]
            b = nums[N - 1 - i]
            counter[a + b] += 1
            mins.append(min(a, b))
            maxs.append(max(a, b))

        mins.sort()
        maxs.sort()

        res = N

        for c in range(2 * 1, 2 * limit + 1):
            left = (N >> 1) - bisect_left(mins, c)
            right = bisect_left(maxs, c - limit)

            curr = (N >> 1) + left + right - counter[c]

            res = min(res, curr)

        return res


# -------------------------------

# [Summary]

# 이진탐색의 극 응용.
# 발상의 수준이 매우 높은 문제이다.
# 아, 그정돈 아닌거같기도 하고?
# 둘다 바꿔야 하는 경우를 정의해내는게 포인트.


# [Review]

# 모르겠다. 존나 어렵네. 이해가 되긴 하는데 발상은 좀.
# 이건 적어도 플레는 될거같은데? 적어도?
