# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# --------------------------------------------------------

# vertex, edge
V, E = map(int, input().split())
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


def preorder_traversal(N):
    if N:
        print("%d" % N, end=" ")
        preorder_traversal(Tree[N][0])
        preorder_traversal(Tree[N][1])


preorder_traversal(1)
print()
print(Tree)
