# Authored by : marigold2003
# Date : 2026-11-10 ~ 11-12

"""
-----------------------------------------------------------------------------------------------------------------------------

프로그래밍 과제를 C/C++ 외에 Python으로도 작성할 수 있도록 허용합니다. Python으로 제출하는 학생은 아래 사항을 반드시 지켜 주시기 바랍니다.

채점은 Python 3.14를 기준으로 합니다. 따라서 코드는 Python 3.14 이하 버전의 문법으로 작성해야 하며, 제출 전에 Python 3.14에서 정상적으로 실행되는지 반드시 확인하기 바랍니다. PyCharm이나 VS Code 같은 개발 도구는 무엇을 사용해도 상관없습니다. 입력은 표준 입력으로 받고, 출력은 표준 출력으로 해야 합니다. 소스 파일은 UTF-8로 저장해 주세요.

라이브러리는 Python에 기본으로 포함된 표준 라이브러리만 사용할 수 있습니다.
numpy, pandas처럼 별도로 설치해야 하는 외부 패키지를 사용한 코드는 채점 환경에서 실행되지 않으므로 0점 처리됩니다.

실행 시간 제한은 프로그래밍 언어와 관계없이 동일하게 적용합니다. Python으로 작성했다고 해서 실행 시간을 더 주지 않으니 유의하기 바랍니다.

프로그램 파일 이름은 과제와 관계없이 main.py로 고정합니다. 코드 최상단에는 주석으로 학번과 이름을 작성해 주세요(예: # 20231234 홍길동).
채점 방식은 C/C++과 같습니다. 과제별로 테스트 데이터 5개로 채점하며, 하나당 2점, 만점은 10점입니다. 입력 형식과 출력 형식을 엄격히 지켜 주시기 바랍니다.

-----------------------------------------------------------------------------------------------------------------------------
"""

import sys

input = sys.stdin.readline


# [Summary] 제목

#


def main() -> None:

    # [Ideas]

    #

    ##########

    string = list(input().rstrip())
    n = int(input())

    V_to_VV = dict()  # A -> BC 문법
    # V_to_T = dict()  # A -> a 문법 형태는 사용을 안 했다.
    VV_to_V = dict()  # BC : A
    T_to_V = dict()  # a : A

    for _ in range(n):
        # 여기서 들어오는게 길이가 5면 변수, 4면(5가 아니면) 알파벳이다.
        production = input().rstrip()

        if len(production) == 5:
            if production[0] not in V_to_VV:
                V_to_VV[production[0]] = set()
            V_to_VV[production[0]].add(production[3:])
            if production[3:] not in VV_to_V:
                VV_to_V[production[3:]] = set()
            VV_to_V[production[3:]].add(production[0])
        else:
            # if c[0] not in V_to_T:
            #     V_to_T[c[0]] = set()
            # V_to_T[c[0]].add(c[3])
            if production[3] not in T_to_V:
                T_to_V[production[3]] = set()
            T_to_V[production[3]].add(production[0])

    length = len(string)
    # CYK를 돌릴 DP테이블 생성
    dp = [[set() for _ in range(length)] for _ in range(length)]

    # 길이 1의 부분문자열을 우선 유도
    for i in range(length):
        substring = string[i]

        # T에 속하지 않는 알파벳을 요구하면 불가
        if substring not in T_to_V:
            print("no")
            return

        # 부분문자열을 유도하는 변수들을 dp[i][i]에 넣어줘야함.
        dp[i][i] |= T_to_V[substring]

    # ### 길이 2인 부분문자열부터 dp로 쌓기 ###
    # i는 부분문자열 길이 -1
    for i in range(1, length):

        # j는 부분문자열의 인덱스 시작점
        for j in range(length - i):
            substring = string[j : j + i + 1]
            # print(substring)

            # j에서 선택된 부분문자열을 두 영역으로 나누는 경우의 수
            for k in range(i):
                # 부분문자열 형태 출력용
                # left = substring[: k + 1]
                # right = substring[k + 1 :]
                # print(left, right, j, j + i, k)

                can_derive_left = dp[j][j + k]
                can_derive_right = dp[j + k + 1][j + i]
                # print(can_derive_left)
                # print(can_derive_right)

                # 조합을 진행하기 전에, 한쪽이라도 유도되지 않으면 무시한다.
                if not can_derive_left:
                    continue
                if not can_derive_right:
                    continue

                # 가능한 조합들을 전부 넣는다.
                comb_VV = [V1 + V2 for V1 in can_derive_left for V2 in can_derive_right]

                for vv in comb_VV:
                    if vv not in VV_to_V:
                        continue
                    dp[j][j + i] |= VV_to_V[vv]

    # dp테이블 출력 확인용
    # for row in dp:
    #     print(row)

    # 알파벳을 output에 모으고, 진행중인 변수를 stack에 쌓는다.
    output = ""
    stack = []

    # 이 재귀함수는 V를 VV 또는 T로 반드시 유도한다.
    def recursion(V, start, end):
        nonlocal output

        # 재귀가 돌 때마다 왼쪽 변수부터 알파벳으로 처리된 진행상황을 출력한다.
        print(output + "".join(stack[::-1]), "\n=>", end="")

        # 시작과 끝이 같으면 알파벳이다.
        if start == end:
            stack.pop()
            output += string[start]
            return

        # 지금 들어온 변수가 어떤 VV로 바뀔 수 있는지 확인
        candidate_VV = V_to_VV[V]

        # 현재 사용중인 인덱스를 둘로 나누는 경우의 수
        for i in range(1, end + 1 - start):
            # left = string[start : start + i]
            # right = string[start + i : end + 1]

            # 바뀔 수 있는 모든 VV에 대해서 검사
            for VV in candidate_VV:
                if VV[0] in dp[start][start + i - 1] and VV[1] in dp[start + i][end]:
                    # print(left, right)

                    stack.pop()
                    stack.append(VV[1])
                    stack.append(VV[0])

                    # 왼쪽을 먼저 유도한 후, 오른쪽을 유도한다.
                    recursion(VV[0], start, start + i - 1)
                    recursion(VV[1], start + i, end)

                    # 하나의 경우만 찾아도 된다.
                    return

    # S가 dp[0][-1]에 포함되어있다면 w를 유도한다.
    if "S" in dp[0][-1]:
        print("yes")

        stack.append("S")
        # 이 재귀는 반드시 진행된다. S가 w로 유도됨은 증명됨
        recursion("S", 0, length - 1)

        # 최종 결과를 출력해준다.
        print(output)

    # S가 dp[0][-1]에 포함되지 않는다면 w를 유도할 수 없다.
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
