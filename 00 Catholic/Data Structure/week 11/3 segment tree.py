def buildST():
    for i in range(howmany):
        Tree[howmany + i] = Data[i]
    for i in range(howmany - 1, 0, -1):
        # 두 자식의 합을 부모에 넣는다.
        Tree[i] = Tree[i << 1] + Tree[i << 1 | 1]


def updateST(where, value):
    # ST에는 howmany를 더해줘야 원래 data의 위치가 나온다.
    where = where + howmany
    Tree[where] = value

    # where의 부모는 rshift, 형제는 xor1
    while where > 1:
        Tree[where >> 1] = Tree[where] + Tree[where ^ 1]
        where >>= 1


Data = [1, 2, 3, 4, 5]
howmany = len(Data)

Tree = [0] * (2 * howmany)

buildST()
print(Tree)
updateST(2, 9)
print(Tree)
