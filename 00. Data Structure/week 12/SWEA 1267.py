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
# Problem Number : 1267


# [Summary] 1267. [S/W 문제해결 응용] 10일차 - 작업순서

# 주어진 방향그래프를 위상정렬해 출력하시오.


def main() -> None:

    # [Ideas]

    # 위상정렬하자. inDegree 진입차수를 구하자.

    from collections import deque

    ##########

    T = 10
    for tc in range(1, T + 1):

        V, E = map(int, input().split())
        Data = list(map(int, input().split()))
        Graph = {i: [] for i in range(1, V + 1)}

        # 진입차수 기록
        inDeg = [0] * (V + 1)
        for i in range(E):
            _from, _to = Data[i * 2], Data[i * 2 + 1]
            Graph[_from].append(_to)
            inDeg[_to] += 1

        # 위상정렬 시작
        result = []
        queue = deque([i for i in range(1, V + 1) if not inDeg[i]])

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for nei in Graph[curr]:
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    queue.append(nei)

        print(f"#{tc} {' '.join(map(str, result))}")

    ##########

    return


# [Review]

# 위상정렬을 연습하기 좋은 문제.
# 알고 있다면 쉽겠지만, 존재를 모르는 상태에서 접근하려면 다른 방법이 필요하다.


if __name__ == "__main__":
    main()
