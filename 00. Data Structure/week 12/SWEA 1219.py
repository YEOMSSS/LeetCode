import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-22
# Problem Number : 1219


# [Summary] 1219. [S/W 문제해결 기본] 4일차 - 길찾기

# 단방향 그래프가 주어진다.
# 0에서 99로 이동하는 경로가 존재하는지 판단하시오.


def main() -> None:

    # [Ideas]

    # 이건 dfs를 사용하고 싶다.
    # 평소 파이썬으로 dfs를 할 때는 stack을 이용했지만,
    # 이번에는 배운대로 dfsR을 사용해보자.

    from collections import defaultdict

    ##########

    T = 10

    def dfsR(curr):
        visited.add(curr)

        for nei in Graph[curr]:
            if nei == 99:
                return 1
            if nei in visited:
                continue
            if dfsR(nei):
                return 1
        return 0

    for tc in range(1, T + 1):

        tc, E = map(int, input().split())
        Data = list(map(int, input().split()))

        Graph = defaultdict(list)
        for i in range(E):
            u, v = Data[i * 2], Data[i * 2 + 1]
            Graph[u].append(v)

        # Graph를 고정으로 만들지 않았으니 visited도 set으로 사용한다.
        visited = set()
        result = dfsR(0)
        print(f"#{tc} {result}")

    ##########

    return


# [Review]

# 재귀 dfs를 이용한 기조척인 문제.
# 문제 내에서 주는 가이드라인보다 효율적인 방법을 선택해 보자.


if __name__ == "__main__":
    main()
