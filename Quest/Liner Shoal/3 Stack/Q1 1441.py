# -------------------------------
# Link : https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-18
# Problem Number : 1441

# -------------------------------

# [Problem] 스택 연산으로 배열 만들기

# 빈 stack에 1~n을 차례로 append받고, 원한다면 pop을 할 수 있다.
# target과 동일한 형태의 stack을 만들기 위한 과정을 출력하시오.


# [Intuition]

# 넣다뺐다 계속하면 되겠네.
# target이랑 한칸씩 비교하면서 가자.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        stack = []
        idx = -1
        len_target = len(target)

        for i in range(1, n + 1):

            idx += 1
            if idx >= len_target:
                break
            stack.append(i)
            result.append("Push")

            if stack[idx] != target[idx]:
                idx -= 1
                stack.pop()
                result.append("Pop")

        return result


# -------------------------------

# [Summary]

# 한칸씩 이동하면서 인덱스를 맞춘다.
# break 타이밍에 유의.


# [Review]

# 아주 어렵진 않다. 스택이 뭔지는 알잖아?
