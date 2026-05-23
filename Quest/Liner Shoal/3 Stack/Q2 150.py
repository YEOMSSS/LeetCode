# -------------------------------
# Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-23
# Problem Number : 150

# -------------------------------

# [Problem] Evaluate Reverse Polish Notation

# RPN은 후위 표기식이다.
# 입력으로 정상적인 RPN이 들어올 때, 결과를 계산해 return하시오.


# [Intuition]

# 숫자면 stack에 append하고, operator면 pop 두번 해서 계산해서 다시 넣고.


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


def calc(op, a, b):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return int(a / b)


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        result = 0
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                # print(a,b)
                stack.append(calc(t, a, b))
            else:
                stack.append(int(t))

        return stack.pop()


# -------------------------------

# [Summary]

# 스택을 이용한 후위표기식 연산.


# [Review]

# 후위 표기식 연산도 오랜만이네.
