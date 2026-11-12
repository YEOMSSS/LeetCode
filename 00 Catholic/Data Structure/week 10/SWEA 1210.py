import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-06-05
# Problem Number : 1210


# [Summary] 1210. [S/W 문제해결 기본] 2일차 - Ladder1

# 100*100 board 가 0과 1로 채워져 있다.
# 1이 사다리다. 사다리타기 게임을 진행하시오.
# 10개의 테스트케이스가 진행된다.


def main() -> None:

    # [Ideas]

    ##########

    # 위로 올라가면서 찾을 것이므로, 아래는 확인할 필요가 없다.
    # 좌우는 상보다 우선된다.
    dy = [0, 0, -1]
    dx = [-1, 1, 0]

    def isPossible(y, x):
        # 사다리를 벗어날 수 없다.
        if not 0 <= y < 100:
            return False
        if not 0 <= x < 100:
            return False
        # 사다리가 1이어야 이동할 수 있다.
        if ladder[y][x] == 0:
            return False
        return True

    def GetSome(y, x):
        ladder[y][x] = 0
        if y == 0:
            print(f"#{tc} {x}")
            return

        for dir in range(3):
            # 좌, 우, 상 순서로 검사하게 된다.
            newY = y + dy[dir]
            newX = x + dx[dir]

            # 좌우이동이 가능하면 이동하고, 둘이 불가능해야 상이동이 가능하다.
            if isPossible(newY, newX):
                GetSome(newY, newX)
                # 여기에 return이 없으면 가로선을 무시하고 위로 올라간다.
                return

    for _ in range(10):
        tc = int(input())

        ladder = [list(map(int, input().split())) for _ in range(100)]

        y = 99
        # 99행에서 시작점인 2를 찾는다.
        x = ladder[99].index(2)

        GetSome(y, x)

    ##########

    return


# [Review]

# 배운 대로 작성해보자.


if __name__ == "__main__":
    main()
