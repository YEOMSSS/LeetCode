# Authored by : marigold2003
# Date : 2026-11-10


import sys

input = sys.stdin.readline


# [Summary] 제목

#


def main() -> None:

    # [Ideas]

    #

    ##########

    string = input().strip()
    length = len(string)
    n = int(input())

    # 문법을 저장할 때, BC:A랑 a:A로 저장하는게 더 편해보이는데?
    # 아닌가, 양방향 딕셔너리를 만들어야하는가? 애매하다, 애매해.
    V_to_VV = dict()  # A -> BC 문법
    V_to_T = dict()  # A -> a 문법

    VV_to_V = dict()  # BC : A
    T_to_V = dict()  # a : A

    for _ in range(n):
        c = input().strip()  # 여기서 들어오는게 길이가 5면 변수, 4면 알파벳이다.
        if len(c) == 5:
            if c[0] not in V_to_VV:
                V_to_VV[c[0]] = set()
            V_to_VV[c[0]].add(c[3:])
            if c[3:] not in VV_to_V:
                VV_to_V[c[3:]] = set()
            VV_to_V[c[3:]].add(c[0])
        else:
            if c[0] not in V_to_T:
                V_to_T[c[0]] = set()
            V_to_T[c[0]].add(c[3])
            if c[3] not in T_to_V:
                T_to_V[c[3]] = set()
            T_to_V[c[3]].add(c[0])

    dp = [[set() for _ in range(length)] for _ in range(length)]

    # 출력 확인용
    # print(V_to_VV)
    # print(V_to_T)
    # print(VV_to_V)
    # print(T_to_V)

    # aabbb
    # 00 11 22 33 44
    # 01 12 23 34
    # 02 13 24
    # 03 14
    # 04

    # 길이 1의 부분문자열을 우선 유도
    for i in range(length):
        substring = string[i]

        # T에 속하지 않는 알파벳을 요구하면 불가
        if substring not in T_to_V:
            print("no")
            return

        # temp를 유도하는 변수들을 dp[i][i]에 넣어줘야함.
        dp[i][i] |= T_to_V[substring]

    # 길이 2인 부분문자열부터 dp로 쌓기

    # 부분문자열 길이 -1
    for i in range(1, length):

        # 부분문자열 개수
        for j in range(length - i):
            substring = string[j : j + i + 1]
            # print(substring)

            # 두 영역으로 나누는 경우의 수
            for k in range(i):
                # 부분문자열 형태 출력용
                # left = substring[: k + 1]
                # right = substring[k + 1 :]
                # print(left, right, j, j + i, k)

                can_derive_left = dp[j][j + k]
                can_derive_right = dp[j + k + 1][j + i]

                # print(can_derive_left)
                # print(can_derive_right)

                can_VV = [V1 + V2 for V1 in can_derive_left for V2 in can_derive_right]

                for vv in can_VV:
                    if vv not in VV_to_V:
                        continue
                    dp[j][j + i] |= VV_to_V[vv]
        # print()

    # # 출력 확인용
    # for row in dp:
    #     print(row)

    output = ""
    stack = []

    def recursion(V, start, end):
        nonlocal output
        print(output + "".join(stack[::-1]), "\n=>", end="")

        if start == end:
            output += string[start]
            stack.pop()
            return

        derived_set = V_to_VV[V]
        # print(derived_set)

        for i in range(1, end + 1 - start):
            # left = string[start : start + i]
            # right = string[start + i : end + 1]

            for VV in derived_set:
                if VV[0] in dp[start][start + i - 1] and VV[1] in dp[start + i][end]:
                    stack.pop()
                    stack.append(VV[1])
                    stack.append(VV[0])

                    # print(left, right)
                    recursion(VV[0], start, start + i - 1)
                    recursion(VV[1], start + i, end)
                    return

    if "S" in dp[0][-1]:
        print("yes")

        stack.append("S")
        recursion("S", 0, length - 1)

        print(output)

    else:
        print("no")

    ##########

    return


# [Review]

#


if __name__ == "__main__":
    main()


"""
aabbb
5
S->AB
A->BB
A->a
B->AB
B->b
"""
