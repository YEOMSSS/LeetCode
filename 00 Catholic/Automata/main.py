# 202221119 염준하

import sys

input = sys.stdin.readline


def main() -> None:

    ##########

    string = list(input().rstrip())
    n = int(input())

    A_to_BC = dict()  # A -> BC를 A : BC 형태로 저장
    ABC_rules = []  # A -> BC를 (A, B, C) 형태로 저장
    a_to_A = dict()  # a -> A를 a : A 형태로 저장

    for _ in range(n):
        # 이 프로덕션의 길이가 5면 A -> BC, 4면 A -> a 형태이다.
        P = input().rstrip()

        if len(P) == 5:
            if P[0] not in A_to_BC:
                A_to_BC[P[0]] = set()
            A_to_BC[P[0]].add(P[3:])
            ABC_rules.append((P[0], P[3], P[4]))
        else:
            if P[3] not in a_to_A:
                a_to_A[P[3]] = set()
            a_to_A[P[3]].add(P[0])

    length = len(string)
    # CYK를 돌릴 DP테이블 생성, 2차원 배열의 각 칸을 공집합으로 초기화
    # dp[i][j]는 string[i : j + 1]를 유도할 수 있는 변수들의 집합
    dp = [[set() for _ in range(length)] for _ in range(length)]

    # 길이 1의 부분문자열을 먼저 유도한다.
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

            # j에서 선택된 부분문자열을 두 영역으로 나누는 경우의 수
            for k in range(i):

                # 왼쪽 부분문자열과 오른쪽 부분문자열을 유도하는 변수 찾기
                left = dp[j][j + k]
                right = dp[j + k + 1][j + i]

                # 조합을 진행하기 전에, 한쪽이라도 유도되지 않으면 무시한다.
                if not left or not right:
                    continue

                for A, B, C in ABC_rules:
                    if B in left and C in right:
                        dp[j][j + i].add(A)

    # 알파벳을 output에 쌓고, 진행중인 변수를 stack에 쌓는다.
    output = []
    stack = []

    # recursion(start, end)는 스택의 top 변수가 string[start : end + 1]을 유도하도록 전개한다.
    # 이 재귀함수는 A가 BC 또는 a로 유도될 때만 실행된다.
    def recursion(start, end):
        # 재귀가 돌 때마다 왼쪽 변수부터 알파벳으로 처리된 진행상황을 출력한다.
        # stack의 top이 문장형태의 최좌측 변수이므로 stack[::-1]이 변수들을 왼쪽부터 나열한 문자열이다.
        print("".join(output + stack[::-1]))
        print("=>", end="")

        # 최좌측 변수를 꺼내준다.
        A = stack.pop()

        # 시작과 끝이 같으면 알파벳이다.
        if start == end:
            output.append(string[start])
            return

        # 지금 들어온 A가 어떤 BC로 바뀔 수 있는지 확인
        cand_BC = A_to_BC[A]

        # 현재 사용중인 인덱스를 둘로 나누는 경우의 수
        for i in range(1, end + 1 - start):

            # 바뀔 수 있는 모든 BC에 대해서 검사
            for BC in cand_BC:
                if BC[0] in dp[start][start + i - 1] and BC[1] in dp[start + i][end]:

                    # B가 top이 되어 먼저 전개되도록 C를 먼저 append한다.
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
        # 이 재귀는 반드시 정상 작동한다. 현재 S가 w로 유도됨은 자명하기 때문
        recursion(0, length - 1)

        # 최종 결과를 출력해준다.
        print("".join(output))

    # S가 dp[0][-1]에 포함되지 않는다면 w를 유도할 수 없다.
    else:
        print("no")

    ##########

    return


if __name__ == "__main__":
    main()
