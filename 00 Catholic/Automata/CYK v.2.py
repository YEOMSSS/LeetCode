# Authored by : 염준하
# Date : 2026-11-10 ~ 11-18


import sys

input = sys.stdin.readline


def main() -> None:

    ##########

    string = list(input().rstrip())
    n = int(input())

    A_to_BC = dict()  # A -> BC 문법
    # BC_to_A = dict()  # BC : A 로는 저장할 필요 없다.
    # A_to_a = dict()  # A -> a 문법 형태는 사용을 안 했다.
    a_to_A = dict()  # a : A

    rules = []  # (A, B, C) 형태로 저장

    for _ in range(n):
        # 여기서 들어오는게 길이가 5면 A -> BC, 4면 A -> a이다.
        P = input().rstrip()

        if len(P) == 5:
            if P[0] not in A_to_BC:
                A_to_BC[P[0]] = set()
            A_to_BC[P[0]].add(P[3:])
            rules.append((P[0], P[3], P[4]))
            # if P[3:] not in BC_to_A:
            #     BC_to_A[P[3:]] = set()
            # BC_to_A[P[3:]].add(P[0])
        else:
            # if P[0] not in A_to_a:
            #     A_to_a[P[0]] = set()
            #     A_to_a[P[0]].add(P[3])
            if P[3] not in a_to_A:
                a_to_A[P[3]] = set()
            a_to_A[P[3]].add(P[0])

    length = len(string)
    # CYK를 돌릴 DP테이블 생성, 2차원 배열의 각 칸을 공집합으로 초기화
    dp = [[set() for _ in range(length)] for _ in range(length)]

    # 길이 1의 부분문자열을 우선 유도
    for i in range(length):
        substring = string[i]

        # T에 속하지 않는 알파벳을 요구하면 불가
        if substring not in a_to_A:
            print("no")
            return

        # 부분문자열을 유도하는 변수들을 dp[i][i]에 넣어줘야함.
        dp[i][i] |= a_to_A[substring]

    # ##### 길이 2인 부분문자열부터 dp로 쌓기 #####
    # i는 부분문자열 길이 -1
    for i in range(1, length):

        # j는 부분문자열의 인덱스 시작점
        for j in range(length - i):

            # # 부분문자열 형태 출력용
            # # substring = string[j : j + i + 1]
            # # print(substring)

            # # j에서 선택된 부분문자열을 두 영역으로 나누는 경우의 수
            # for k in range(i):
            #     # 부분문자열 형태 출력용
            #     # left = substring[: k + 1]
            #     # right = substring[k + 1 :]
            #     # print(left, right, j, j + i, k)

            #     can_derive_left = dp[j][j + k]
            #     can_derive_right = dp[j + k + 1][j + i]
            #     # print(can_derive_left)
            #     # print(can_derive_right)

            #     # 조합을 진행하기 전에, 한쪽이라도 유도되지 않으면 무시한다.
            #     if not can_derive_left:
            #         continue
            #     if not can_derive_right:
            #         continue

            #     # 가능한 조합들을 전부 넣는다.
            #     comb_BC = [B + C for B in can_derive_left for C in can_derive_right]

            #     for BC in comb_BC:
            #         if BC not in BC_to_A:
            #             continue
            #         dp[j][j + i] |= BC_to_A[BC]

            # 굳이 BC를 합쳐서 만들 필요 없이, B와 C를 따로 보면 된다.
            # comb_BC를 만들 필요가 없다는 것임.

            # j에서 선택된 부분문자열을 두 영역으로 나누는 경우의 수
            for k in range(i):

                # 왼쪽 부분문자열과 오른쪽 부분문자열을 유도하는 변수 찾기
                left = dp[j][j + k]
                right = dp[j + k + 1][j + i]

                # 조합을 진행하기 전에, 한쪽이라도 유도되지 않으면 무시한다.
                if not left or not right:
                    continue

                for A, B, C in rules:
                    if B in left and C in right:
                        dp[j][j + i].add(A)

    # dp테이블 출력 확인용
    # for row in dp:
    #     print(row)

    # 알파벳을 output에 모으고, 진행중인 변수를 stack에 쌓는다.
    output = ""
    stack = []

    # 이 재귀함수는 A를 BC 또는 a로 반드시 유도한다.
    def recursion(start, end):
        nonlocal output

        # 재귀가 돌 때마다 왼쪽 변수부터 알파벳으로 처리된 진행상황을 출력한다.
        print(output + "".join(stack[::-1]))
        print("=>", end="")

        # 최좌측 변수를 꺼내준다.
        A = stack.pop()

        # 시작과 끝이 같으면 알파벳이다.
        if start == end:
            output += string[start]
            return

        # 지금 들어온 A가 어떤 BC로 바뀔 수 있는지 확인
        cand_BC = A_to_BC[A]

        # 현재 사용중인 인덱스를 둘로 나누는 경우의 수
        for i in range(1, end + 1 - start):
            # left = string[start : start + i]
            # right = string[start + i : end + 1]

            # 바뀔 수 있는 모든 BC에 대해서 검사
            for BC in cand_BC:
                if BC[0] in dp[start][start + i - 1] and BC[1] in dp[start + i][end]:
                    # print(left, right)

                    stack.append(BC[1])
                    stack.append(BC[0])

                    # 왼쪽을 먼저 유도한 후, 오른쪽을 유도한다.
                    recursion(start, start + i - 1)
                    recursion(start + i, end)

                    # 하나의 경우만 찾아도 된다.
                    return

    # S가 dp[0][-1]에 포함되어있다면 w를 유도한다.
    if "S" in dp[0][-1]:
        print("yes")

        stack.append("S")
        # 이 재귀는 반드시 진행된다. S가 w로 유도됨은 증명됨
        recursion(0, length - 1)

        # 최종 결과를 출력해준다.
        print(output)

    # S가 dp[0][-1]에 포함되지 않는다면 w를 유도할 수 없다.
    else:
        print("no")

    ##########

    return


if __name__ == "__main__":
    main()


""" 예제1
aabbb
5
S->AB
A->BB
A->a
B->AB
B->b

yes
S
=>AB
=>aB
=>aAB
=>aaB
=>aaAB
=>aaBBB
=>aabBB
=>aabbB
=>aabbb
"""
