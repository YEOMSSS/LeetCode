# -------------------------------

# Authored by : marigold2003
# Date : 2026-08-29
# Problem Number : 1342

# -------------------------------

# [Problem] Number of Steps to Reduce a Number to Zero

# 짝수면 2로 나누고 홀수면 1을 빼는 것을 반복한다.
# 총 몇 단계가 지나야 0으로 만들 수 있는지 구하시오.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def numberOfSteps(self, num: int) -> int:

        step = 0

        while True:
            if not num:
                return step

            if num % 2:
                num -= 1
            else:
                num //= 2

            step += 1


# -------------------------------

# [Summary]

# 2로 나누고 1로 빼는 걸 직접 시뮬레이션.
# 그리고 스텝을 하나씩 올리면 된다.


# [Review]

# 비트마스킹으로도 풀 수 있을 것 같음.
# 2진수로 바꾸면 되는거 아니냐 그냥?
# 2진수로 바꿔서 1이면 두단계 0이면 한단계 올리면 되네.
# 뭐 마지막에 0이니까 그거만 한단계 낮춰주면 된다.
