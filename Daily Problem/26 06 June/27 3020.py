# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-27
# Problem Number : 3020

# -------------------------------

# [Problem] Find the Maximum Number of Elements in Subset

# 숫자가 주어진 nums가 주어진다.
# 만들 수 있는 2제곱으로 올라갔다 내려오는 규칙성을 띈 가장 긴 배열의 길이를 구하시오.


# [Intuition]

# 홀수개의 1이 연속되어도 가능하다.
# 한 배열에 같은 숫자는 2개만 쓰일 것.

# 1을 선택할 수 있다. 몇 제곱을 하던 1은 가능하니까.
# set을 이용해서 목표하는 값이 있는지 확인하고 개수를 봐야한다.
# 차라리 Counter를 사용하는게 나아보이기도 한다. 2개 이상 있는지 확인이 필요하니까.

# 1이 짝수개일때 주의, 답의 최솟값이 1임에 주의.

# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import Counter

# -------------------------------


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)

        result = max(1, counter[1])
        if result and result % 2 == 0:
            result -= 1

        for n in counter:
            if n == 1:
                continue
            if counter[n] <= 1:
                continue
            temp = 1
            while True:
                n **= 2
                print(n)
                if not counter[n]:
                    break
                if counter[n] == 1:
                    temp += 2
                    break
                temp += 2
            result = max(result, temp)

        return result


# -------------------------------

# [Summary]

# 브루트 포스로 풀었다.


# [Review]

# 시험 끝나고 복귀했다.
# 까먹고 수업평가 안해서 성적 확인이 안돼. 씨이발.
