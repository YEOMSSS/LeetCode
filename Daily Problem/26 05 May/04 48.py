# -------------------------------
# Link : https://leetcode.com/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-04
# Problem Number : 48


# [Problem] Rotate Image

# n*n(<= 20) size의 2d list가 들어온다.
# 시계방향 90도로 회전하되, in-place 알고리즘을 이용하여 새로운 배열을 만들지 않고 회전시키시오.


# [Intuition]

# 가장 위 줄을 저장해두고, 나머지를 복붙하듯 한칸씩 가져오면 된다.
# 우측을 위로, 아래를 우측으로, 좌측을 아래로, 그리고 좌측에는 빼둔 위를 다시 넣으면 된다.

# [Approach]

# 1. n//2회만큼 회전을 0행부터 반복한다.
# 2. 맨 위 행의 왼쪽 칸을 temp에 저장해두고, 거기 들어올 왼쪽 열의 칸을 덮어씌운다.
# 3. 덮어씌우는데 사용한 왼쪽 열의 칸을 아래쪽 행의 칸으로 덮어씌운다.
# 4. 덮어씌우는데 사용한 아래쪽 행의 칸을 오른쪽 열의 칸으로 덮어씌운다.
# 5. 덮어씌우는데 사용한 오른쪽 열의 칸을 저장해둔 temp로 덮어씌우면 4개가 회전한 꼴이 된다.
# 6. 이걸 바꿀 칸 블록의 덩어리만큼 반복한다.


def solve(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    ##########

    n = len(matrix[0])
    for i in range(n // 2):

        for j in range(i + 1, n - i):
            # 상값을 저장해둔다.
            temp = matrix[i][j - 1]

            # 상 <- 좌
            matrix[i][j - 1] = matrix[n - j][i]

            # 좌 <- 하
            matrix[n - j][i] = matrix[n - i - 1][n - j]

            # 하 <- 우
            matrix[n - i - 1][n - j] = matrix[j - 1][n - i - 1]

            # 우 <- 상
            matrix[j - 1][n - i - 1] = temp

    for row in matrix:
        print(row)

    ##########

    return None


# [LeetCode]


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        solve(matrix)


# [Summary]

# 하나를 꺼내 놓고 덮어씌우는 것을 반복한다.
# 인덱스를 어떻게 굴릴 것인지 고민하는 과정이 필요하다.
# 효율적인 알고리즘을 짜는 연습을 할 수 있는 좋은 문제.


# [Review]

# 확실히 문제 질이 좋다.
# 백준이었으면 그냥 2차원배열 하나 새로 만들었을 것 같다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    n = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(n))

    print(solve(matrix))
