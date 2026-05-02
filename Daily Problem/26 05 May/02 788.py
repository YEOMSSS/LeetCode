# -------------------------------
# Link : https://leetcode.com/problems/rotated-digits/description/?envType=daily-question&envId=2026-05-02
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-02
# Problem Number : 788


# [Problem] Rotated Digits

# N(<= 10K)까지의 자연수 안에서 각 자리 숫자를 180도 회전 또는 대칭시켰을 때
# 원본이 아닌 말이 되는 자연수가 나오는 경우의 수를 구하시오.


# [Intuition]

# 2, 5, 6, 9만 가능하다.
# 1, 8, 0은 동일해져서 탈락 3, 4, 7은 회전이 안 된다.

# 이거, dp인거 같다. 많은 범위가 겹치는 걸 볼 수 있다.
# 한 자리를 붙일 때마다 앞 자리에서 가능한 것들에 전부 붙여야 한다.
# 그럼 1의 자리 다 구하고, 4를 곱해주면 10의 자리 개수가 되는거지.
# 그냥 애매하게 잘릴 때만 처리해주면 되겠다.

# 아, 3, 4, 7이 들어가면 아예 불가능이구나?

# 새로운 직관을 하자.
# 어차피 10K인데 그냥 브루트포스를 조져도 되지 않아?
# 347이면 즉시 불가능, 2569 존재하면 합격.

# [Approach]

# 1. 일의 자리 수는 4개이다.
# 2. 십의 자리 수부터는 2,5,6,9를 붙일때는 0-9가 전부 되고, 아닐 땐 dp[i-1]만큼만 된다.
# 3. 목표 N이 될 때까지 남은 걸 처리한다.


# dp로는 좆같아서 더는 못해먹겠다.
def fail(n: int) -> int:

    ##########

    result = 0
    length = len(str(n))
    N = n

    if length == 1:
        for i in range(N + 1):
            if i in [2, 5, 6, 9]:
                result += 1
        return result

    dp = [0] * length
    dp[1] = 4

    for i in range(2, length):
        dp[i] = dp[i - 1] * 2 + 7 ** (i - 1) * 4
    print(dp)

    flag = False

    for _ in range(length):
        curr = N // 10 ** (length - 1)
        N %= 10 ** (length - 1)
        print(curr, N, length, flag)

        if length == 1:
            for i in range(curr + 1):
                if i in [2, 5, 6, 9]:
                    result += 1
                if flag and i in [0, 1, 8]:
                    result += 1
            break

        for i in range(0, curr):
            if i in [2, 5, 6, 9]:
                result += 7 ** (length - 1)
            elif i in [3, 4, 7]:
                pass
            elif i in [0, 1, 8]:
                if flag:
                    result += 7 ** (length - 1)
                else:
                    result += sum(dp[:length])

        if curr in [2, 5, 6, 9]:
            flag = True
        elif curr in [3, 4, 7]:
            break

        if flag and not N:
            result += 1
            break

        length -= 1

    ##########

    return result


# [Approach]

# 1. 1~n을 전부 확인한다.
# 2. 확인할 i를 str로 바꿔 한 자리씩 검사한다.
# 3. 347을 만나면 즉시 불합격 판정을 한다.
# 4. 2569를 만나면 체크해두고, 불합격 판정이 나지 않으면 합격 판정을 한다.


def solve(n) -> int:
    result = 0

    for i in range(1, n + 1):
        flag = False

        for j in str(i):
            j = int(j)

            if j in [3, 4, 7]:
                flag = False
                break

            elif j in [2, 5, 6, 9]:
                flag = True

        if flag:
            result += 1

    return result


# [LeetCode]


class Solution:
    def rotatedDigits(self, n: int) -> int:
        return solve(n)


# [Summary]

# dp 문제다.
# 그냥 씨발 브루트포스로 풀자.


# [Review]

# 왤케 어렵지.
# 화가 난다 그냥.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    N = int(input())

    print(solve(N))
