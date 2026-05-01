# Authored by : marigold2003
# Date : 2026-05-01
# Link : https://www.acmicpc.net/problem/24051


import sys

input = sys.stdin.readline


# [Summary] 알고리즘 수업 - 삽입 정렬 1

# 삽입 정렬 과정에서 K번째 저장되는 값을 출력하시오.


def insertion_sort(arr, n, k):
    cnt = 0

    for i in range(1, n):

        # 비교를 시작할 위치를 i-1 인덱스로 잡는다.
        loc = i - 1
        # current를 들어올려서 왼쪽으로 간다.
        curr = arr[i]

        # 왼쪽으로 끝까지 가거나 자신보다 작은게 나오기 전까지 왼쪽으로 이동한다.
        while loc >= 0 and curr < arr[loc]:

            # 자신보다 큰 놈을 자기 자리로 당겨온다.
            arr[loc + 1] = arr[loc]

            # cnt 증가
            cnt += 1
            if cnt == k:
                return arr[loc + 1]

            # 자신은 한 칸 왼쪽으로 간다.
            loc -= 1

        # 이동이 있는 경우만 내려놓기로 cnt 소모
        if loc + 1 != i:
            arr[loc + 1] = curr

            # cnt 증가
            cnt += 1
            if cnt == k:
                return arr[loc + 1]

    return -1


def main() -> None:

    ##########

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    print(insertion_sort(arr, N, K))

    ##########

    return


# [Review]

# 백준의 부활을 기다려본다.


if __name__ == "__main__":
    main()
