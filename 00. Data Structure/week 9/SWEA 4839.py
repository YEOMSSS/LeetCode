import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\99. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-01
# Problem Number : 4839


# [Summary] 4839. [S/W 문제해결 기본] 2일차 - 이진탐색

# 책의 총 페이지 수가 주어진다. 책은 1페이지부터 존재한다.
# A와 B가 각각 이분탐색을 이용하여 페이지를 찾을 때,
# 더 적은 횟수의 탐색으로 원하는 페이지를 찾는 사람이 승리한다.

# 승자를 출력하시오. 비기면 0을 출력한다.

# 책이 400페이지인 경우
# 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
# c가 찾는 쪽 번호가 되면 탐색을 멈춘다.


def main() -> None:

    # [Ideas]

    # 전형적인 이분탐색 문제이다.
    # while 반복문을 이용해 풀어보자.

    ##########

    T = int(input())

    def bsearch(P, target):
        start = 1
        end = P

        cnt = 0
        while start <= end:
            mid = (start + end) // 2
            cnt += 1

            if mid == target:
                return cnt
            # 작으면 범위를 늘려야 한다.
            elif mid < target:
                start = mid  # + 1
            # 크면 범위를 줄여야 한다.
            else:
                end = mid  # - 1

        return 0

    for tc in range(1, T + 1):
        P, A, B = map(int, input().split())

        cntA = bsearch(P, A)
        cntB = bsearch(P, B)

        result = 0
        if cntA < cntB:
            result = "A"
        elif cntA > cntB:
            result = "B"

        print(f"#{tc} {result}")

    ##########

    return


# [Review]

# 오랜만에 풀어보는 정석 이분탐색 찾기이다.
# 값이 범위에 존재함이 보장되어 편하다.

# 문제에 함정이 있다. mid-1과 mid+1로 가는 게 아니라
# start와 end를 그냥 mid로 만드는 문제였다.


if __name__ == "__main__":
    main()
