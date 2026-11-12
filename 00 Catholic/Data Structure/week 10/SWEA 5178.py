import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-10
# Problem Number : 5178


# [Summary] 5178. [S/W 문제해결 기본] 8일차 - 노드의 합

# 리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음,
# 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.


def main() -> None:

    # [Ideas]

    # 바텀업처럼 생긴 것이, 재귀 쓰기 딱 좋아보인다.

    ##########

    T = int(input())

    def recursion(N):
        # 리프노드에서 반환한다.
        if arr[N] != -1:
            return arr[N]
        # 자식노드의 합을 구한다.
        curr = recursion(N * 2) + recursion(N * 2 + 1)
        return curr

    for tc in range(1, T + 1):
        N, M, L = map(int, input().split())
        arr = [-1] * (N + 2)

        # 노드 개수가 홀수일 경우 마지막 리프노드를 0으로 만들어줘야 한다.
        arr[-1] = 0

        for _ in range(M):
            leaf, val = map(int, input().split())
            arr[leaf] = val

        result = recursion(L)
        print(f"#{tc} {result}")

    ##########

    return


# [Review]

# 배열로 만든 트리의 원리를 이용했다.
# 이제 보니 세그먼트트리였네.


if __name__ == "__main__":
    main()
