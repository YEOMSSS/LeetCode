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
# Problem Number : 5174


# [Summary] 5174. [S/W 문제해결 기본] 8일차 - subtree

# 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.


def main() -> None:

    # [Ideas]

    # 트리 배열 만드는 템플릿을 그대로 가져와서
    # 재귀로 노드 개수를 세자.

    ##########

    T = int(input())

    # 노드 개수를 세는 재귀함수
    def count_node(n):
        if not n:
            return 0
        else:
            return 1 + count_node(Tree[n][0]) + count_node(Tree[n][1])

    for tc in range(1, T + 1):

        E, N = map(int, input().split())
        V = E + 1
        Tree = [[0] * 5 for _ in range(V + 1)]
        Data = list(map(int, input().split()))

        for i in range(V):
            Tree[i][3] = Tree[i][4] = -1

        # 루트노드 레벨 처리
        Tree[1][4] = 0

        for i in range(E):
            parent, child = Data[i * 2], Data[i * 2 + 1]

            if Tree[parent][0] == 0:

                # 부모의 왼쪽 자식을 채우고, 차수를 하나 올린다.
                Tree[parent][0] = child
                Tree[parent][2] += 1

                # 자식에 부모 정보를 입력하고, 레벨을 부모레벨+1로 한다.
                Tree[child][3] = parent
                Tree[child][4] = Tree[parent][4] + 1

            else:  # 첫번째 자식이 차 있는 경우

                # 부모의 오른쪽 자식을 채우고, 차수를 하나 올린다.
                Tree[parent][1] = child
                Tree[parent][2] += 1

                # 자식에 부모 정보를 입력하고, 레벨을 부모레벨+1로 한다.
                Tree[child][3] = parent
                Tree[child][4] = Tree[parent][4] + 1

        print(f"#{tc} {count_node(N)}")

    ##########

    return


# [Review]

# 템플릿 한 번 잘 짜두니 이렇게 편할 수가.


if __name__ == "__main__":
    main()
