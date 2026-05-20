import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-20
# Problem Number : 1238


# [Summary] 1238. [S/W 문제해결 기본] 10일차 - Contact

# 입력된 bfs에서 주어진 정점에서 bfs를 진행할 때
# 가장 늦게 접근되는 정점 중 최댓값을 구하시오.


def main() -> None:

    # [Ideas]

    # distance를 구하는 문제이다.
    # 정점은 최대 100개이고, 부여될 수 있는 번호 역시 최대 100이다.

    ##########

    from collections import deque, defaultdict

    def bfs(start):

        queue = deque()
        Dist: list = [None] * 101
        # distance를 저장
        DistDict = defaultdict(list)

        queue.append(start)
        Dist[start] = 0
        DistDict[0].append(start)

        while queue:
            curr = queue.popleft()

            for nei in Graph[curr]:
                if Dist[nei] is not None:
                    continue
                Dist[nei] = Dist[curr] + 1
                DistDict[Dist[curr] + 1].append(nei)
                queue.append(nei)

        return max(DistDict[Dist[curr]])

    T = 10
    for tc in range(1, T + 1):

        N, start = map(int, input().split())
        Data = list(map(int, input().split()))

        Graph = [[] for _ in range(101)]

        for i in range(N // 2):
            u, v = Data[i * 2], Data[i * 2 + 1]
            Graph[u].append(v)

        print(f"#{tc} {bfs(start)}")

    ##########

    return


# [Review]

# visited 대신 distance를 사용하여
# 거리가 기록되었으면 방문했다는 논리로 해결하였다.


if __name__ == "__main__":
    main()
