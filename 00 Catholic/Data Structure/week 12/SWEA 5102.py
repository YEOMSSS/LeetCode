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
# Problem Number : 5102


# [Summary] 5102. [S/W 문제해결 기본] 6일차 - 노드의 거리

# 그래프가 주어진다.
# 출발 노드와 도착 노드가 주어질 때, 둘 사이의 최소 경로의 길이를 출력하시오.
# 그래프에는 끊어진 여러 개의 섬이 존재할 수도 있다.


def main() -> None:

    # [Ideas]

    # 최단경로찾기니까 bfs를 사용해야 한다.
    # distance를 이용해 최단경로를 구해보자.
    # bfs 탐색에 실패하면 서로 끊어진 노드인 것이다.

    # 근데 사실 모든 노드의 distance를 기록해 쌓아올릴 필요는 없다.
    # 이렇게 탐색하는 노드까지의 거리를 구하는 문제는
    # len(queue)가 끝날 때마다 dist+=1을 하는 방식을 주로 사용해 왔다.
    # 둘 다 사용해 볼까? 배운대로 풀까?

    # 둘 다 해보자. len(Queue)+visited vs visited 대신 Dist배열.
    # Dist배열이 더 효율적일거라는 생각은 든다. len(Queue)를 실행하는 시간이 줄어드니까.

    ##########

    from collections import deque

    # len(Queue)를 이용하는 경우
    def bfs1(start):
        Queue = deque()
        visited = [False] * (V + 1)

        Queue.append(start)
        visited[start] = True

        dist = 0
        while Queue:
            for _ in range(len(Queue)):

                curr = Queue.popleft()
                # 탐색 성공 시
                if curr == G:
                    return dist

                for nei in Graph[curr]:
                    if visited[nei]:
                        continue
                    visited[nei] = True
                    Queue.append(nei)

            dist += 1
        # 탐색 실패 시
        return 0

    # visited 대신 distance 배열을 이용하는 경우
    def bfs2(start):
        Queue = deque()
        Dist = [-1] * (V + 1)

        Queue.append(start)
        Dist[start] = 0

        while Queue:
            curr = Queue.popleft()
            if curr == G:
                return Dist[G]

            for nei in Graph[curr]:
                if Dist[nei] != -1:
                    continue
                Dist[nei] = Dist[curr] + 1
                Queue.append(nei)

        # 탐색 실패 시
        return 0

    T = int(input())
    for tc in range(1, T + 1):

        V, E = map(int, input().split())
        Graph = {i: [] for i in range(1, V + 1)}
        for _ in range(E):
            u, v = map(int, input().split())
            Graph[u].append(v)
            Graph[v].append(u)
        S, G = map(int, input().split())

        # print(f"#{tc} {bfs1(S)}")
        print(f"#{tc} {bfs2(S)}")

    ##########

    return


# [Review]

# 두 가지 방법으로 distance를 구해보자.
# visited + len(Queue), visited 대신 Dist


if __name__ == "__main__":
    main()
