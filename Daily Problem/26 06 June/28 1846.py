# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-28
# Problem Number : 1846

# -------------------------------

# [Problem] Maximum Element After Decreasing and Rearranging

# 주어진 숫자 배열을 규칙을 이용해 수정하고, 만들 수 있는 수열에서 가장 큰 수를 반환하시오.

# 수열은 1로 시작해야 한다.
# 양 옆 숫자의 차이는 1 이하여야 한다.
# 숫자는 줄일 수만 있다.
# 배치는 자유롭게 할 수 있다.


# [Intuition]

# 감소와 재배치를 무한으로 할 수 있다. 그리고 제일 큰 걸 뽑으면 된다 이거지.
# 그리고 1로 시작해야 하며, 둘 사이의 차이는 1 이하이다.
# 그 말은? 동일하거나 커지거나. 112233334... 이런게 된다는거지.
# Counter를 사용하면 될 것 같은데? 총 개수보다 작은 애들이 중복으로 몇개인지 확인하자고.

# 아 모르겠다, 그냥 브루트포스해도 될거같은데? 정렬하고 하나씩 보자.
# 정렬하고 1씩 쌓으면서 동일하면 동일한걸로 잇고, 크면 차례에 맞춰서 1 크게 줄이자.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        curr = 0
        for n in arr:
            # 현 차례보다 1 커진 수 vs 현재 값(동일시)
            curr = min(curr + 1, n)

        return curr


# -------------------------------

# [Summary]

# 발상. 떠올리기만 하면 쉬운 문제. 떠올리는 것 자체도 그리 어렵지 않다.


# [Review]

# 바로 풀리는구만. 개쉬운문제였다.
