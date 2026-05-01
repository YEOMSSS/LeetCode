# -------------------------------
# Link : https://leetcode.com/problems/rotate-function/description/?envType=daily-question&envId=2026-05-01
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-01
# Problem Number : 396


# [Problem] Rotate Function

# N(<= 10K) 길이의 정수 리스트가 주어진다.
# 정수는 -100 ~ 100 사이이다.

# 리스트를 시계방향으로 한 칸씩 회전시키면서 자신의 인덱스와 그 값을 곱해 전부 더한다.
# 리스트에서 만들 수 있는 회전값의 최댓값을 구하시오.


# [Intuition]

# 일단 브루트포스처럼 보인다.
# deque로 바꿔서 rotate하면 편해 보인다.
# N번 회전시켜보면 될 듯. 10K번 회전, 10K번 연산.
# 1억회연산이 되려나? 역시 어려울 것 같은데.

# 좀 더 단순하게 생각해보자. 이게 총량이 딱히 변하지 않는다.
# 맨 뒤에있는게 앞으로 오면, *0이 된다. 그리고 나머지는 다 하나씩 더 곱해진다.
# 그럼 맨 뒤에있는거 *N-1을 빼고, sum(nums)-맨 뒤에있는거를 해주면 되겠는데?
# 점화식이 있는 문제였네.

# [Approach]

# 1. nums를 인덱스와 그 값을 곱해 전부 더한 시작값 구하기
# 2. [-1]*(N-1)을 제거하고, 시작값에 sum(nums) - [-1]만큼을 더해주면 다음 회전이 된다.
# 3. [-1]부터 앞으로 가면서 [1]까지 반복한다. [0]의 경우는 시작값이 된다.


def solve(nums: list[int]) -> int:

    ##########

    N = len(nums)
    total = sum(nums)

    # enumerate를 이용해 기본 nums에서 인덱스와 그 값의 곱의 총합 구하기
    curr = sum(map(lambda x: x[0] * x[1], enumerate(nums)))
    maxval = curr

    for i in range(N - 1, 0, -1):

        # curr -= nums[i] * (N - 1)
        # curr += total - nums[i]
        curr += total - nums[i] * N

        # 최댓값 갱신
        maxval = max(maxval, curr)

    ##########

    return maxval


# [LeetCode]


class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        return solve(nums)


# [Summary]

# deque와 rotate를 이용하는 문제 -가 아니었다.
# 수에 겹치는 부분이 많으므로, 간단한 점화식으로 풀 수 있다.


# [Review]

# 리트코드는 난이도가 easy, medium, hard이다 보니
# 동일 난이도 내에서도 많이 갈리는 듯 하다.
# 이제 랜덤 마라톤 대신 daily problem이다.

# 근데 와, 이거 문제가 좋긴 하네!
# 생각을 좀 해야 한다. 중간에 뇌를 멈추면 안 된다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
