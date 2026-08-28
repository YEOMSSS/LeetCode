# -------------------------------

# Authored by : marigold2003
# Date : 2026-08-28
# Problem Number : 412

# -------------------------------

# [Problem] Fizz Buzz

# i가 3과 5로 모두 나눠지는지
# 3으로만인지, 5로만인지, 안나눠지는지 판단하기

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []
        for i in range(1, n + 1):
            if not i % 15:
                answer.append("FizzBuzz")
            elif not i % 5:
                answer.append("Buzz")
            elif not i % 3:
                answer.append("Fizz")
            else:
                answer.append(str(i))

        return answer


# -------------------------------

# [Review]

# 도파민 디톡스가 효과가 있네.
