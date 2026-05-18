# -------------------------------
# Link : https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-06
# Problem Number : 1861

# -------------------------------

# [Problem] Rotating the Box

# m(<=500)*n(<=500) 2차원 arr이 들어온다.
# arr에는 벽*과 돌#이 들어 있다.
# arr을 시계로 90도 회전해서 중력에 의해 돌이 떨어진 상태의
# arr을 return하시오.


# [Intuition]

# 한줄한줄 밀면 된다.
# 돌리기 전에 row상태로 오른쪽으로 미는게 더 편할듯.
# row를 *이 나오기 전까지 확인해서 빈칸과 #의 개수를 세고
# *이 나오면 new list에 다시 밀어넣으면 된다.
# 그리고 zip으로 회전한다.

# [Approach]

# 1. row를 하나씩 받아 벽이 나올때까지 센다.
# 2-1. 벽이 나오면, 나온 빈칸을 모두 new_row에 넣고 나온 돌도 모두 넣는다.
# 2-2. 벽을 넣고 count를 리셋한다.
# 3. row가 끝나면 남은 count를 확인해 new_row를 전부 채운다.
# 4. new_row를 새 result에 넣는다.
# 5. result를 뒤집어서 zip으로 열기준으로 묶는다.

# -------------------------------


def solve(boxGrid: list[list[str]]) -> list[tuple[str]]:

    ##########

    result = []

    for row in boxGrid:
        new_row = []
        empty = 0
        stone = 0
        for ch in row:
            if ch == "*":
                new_row.extend(["."] * empty)
                new_row.extend(["#"] * stone)
                new_row.append("*")
                empty, stone = 0, 0

            elif ch == ".":
                empty += 1
            else:
                stone += 1

        new_row.extend(["."] * empty)
        new_row.extend(["#"] * stone)
        result.append(new_row)

    rotated_result = list(zip(*result[::-1]))

    ##########

    return rotated_result


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[tuple[str]]:
        return solve(boxGrid)


# -------------------------------

# [Summary]

# 뭔가 떠올리긴 어렵지 않았다.
# 한 행씩 처리하면 됨.
# 90도 회전은 zip이 알아서 잘 해준다.


# [Review]

# 발상을 하는 능력.
# list를 tuple로 출력하는 정도는 괜찮나보다.

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    N = int(input())
    boxGrid = [list(input().split()) for _ in range(N)]

    print(solve(boxGrid))
