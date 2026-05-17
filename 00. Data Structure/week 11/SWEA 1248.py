import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-17
# Problem Number : 1248


# [Summary] 1248. [S/W 문제해결 응용] 3일차 - 공통조상

# 이진 트리에서 임의의 두 정점의 가장 가까운 공통 조상을 찾고,
# 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하시오.


def main() -> None:

    # [Ideas]

    # 정점 둘이 레벨 맞춘 다음에 하나씩 올라가면서 비교해보자.

    ##########

    T = int(input())

    # 노드 개수를 세는 재귀함수
    def count_node(n):
        if not n:
            return 0
        else:
            return 1 + count_node(Tree[n][0]) + count_node(Tree[n][1])

    # 레벨을 구하는 재귀함수
    def level(n):
        if n == -1:
            return 0
        else:
            return 1 + level(Tree[n][3])

    for tc in range(1, T + 1):

        V, E, A, B = map(int, input().split())

        Tree = [[0] * 4 for _ in range(V + 1)]
        Data = list(map(int, input().split()))

        for i in range(V):
            Tree[i][3] = -1

        for i in range(E):
            # 한 줄로 된 입력 받기
            parent, child = Data[i * 2], Data[i * 2 + 1]

            if Tree[parent][0] == 0:

                # 부모의 왼쪽 자식을 채우고, 차수를 하나 올린다.
                Tree[parent][0] = child
                Tree[parent][2] += 1

                # 자식에 부모 정보를 입력
                Tree[child][3] = parent

            else:  # 첫번째 자식이 차 있는 경우

                # 부모의 오른쪽 자식을 채우고, 차수를 하나 올린다.
                Tree[parent][1] = child
                Tree[parent][2] += 1

                # 자식에 부모 정보를 입력
                Tree[child][3] = parent

        Alev, Blev = level(A), level(B)

        while Alev > Blev:
            A = Tree[A][3]
            Alev -= 1
        while Alev < Blev:
            B = Tree[B][3]
            Blev -= 1

        while A != B:
            A = Tree[A][3]
            B = Tree[B][3]
            Blev -= 1
            Alev -= 1

        print(f"#{tc} {A} {count_node(A)}")

    ##########

    return


# [Review]

# 이 템플릿은 레벨이 낮은 순서대로 입력이 들어와야
# 4번째 칸에 레벨이 제대로 저장된다.
# 하여 4번째 칸을 그냥 지워버리고 레벨은 재귀함수로 구함.


if __name__ == "__main__":
    main()
