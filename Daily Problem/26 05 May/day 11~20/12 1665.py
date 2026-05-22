# -------------------------------
# Link : https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/?envType=daily-question&envId=2026-05-12
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-12
# Problem Number : 1665

# -------------------------------

# [Problem] Minimum Initial Energy to Finish Tasks

# [actual, minimum] 으로 이루어진 list인 task가 입력된다.
# actual은 i번째 작업에 필요한 실제 에너지의 양이고,
# minimum은 i번째 작업을 시작하는 데 필요한 최소 에너지의 양이다. actual보다 같거나 크다.
# 작업은 원하는 순서대로 할 수 있으며, 모든 작업을 완료하기 위해 필요한 초기 에너지의 최솟값을 구하시오.


# [Intuition]

# 작업을 원하는 순서대로 할 수 있으니까 그리디일 가능성이 높다.
# 필요 최소에너지양이 높은걸 먼저 하면 되는거잖아.
# 최소초기에너지양을 찾으려면 minimum이 작은것부터 정렬하자고.
# 그리고 누적 actual이랑 다음 minimum으로 계속 갱신하면 되는거 아닌가?
# 뭔가 이런 비슷한 걸 풀어봤던 것 같다. 한 실버상위정도였던듯?

# 예제가 풀이과정이 나오니 역시 편하다.
# 이게 아니라 그 뭐야, 차가 큰거부터 처리해야하는거네.


# [Approach]

# 1. tasks를 m-a 오름차순으로 정렬한다.
# 2. m과 누적된 a값 중 큰 것으로 계속 갱신한다.

# -------------------------------


def solve(tasks: list[list[int]]) -> int:

    ##########

    result = 0

    tasks.sort(key=lambda x: x[1] - x[0])

    for a, m in tasks:
        result = max(result + a, m)
        print(result)

    ##########

    return result


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:

        return solve(tasks)


# -------------------------------

# [Summary]

# 전부 처리한 후 거꾸로 다시 올라가서 처리 전 상태로 만드는 것이다.
# 차이가 큰 거부터 처리되었을테니, 작은 거부터 정렬해서 올라가면 된다.


# [Review]

# 백준에서 비슷한 문제가 실버였던 것 같은데, 난이도 판정 기준이 다른가봐.
# 이게 하드라고? 문제 형태가 좀 다른 거 같긴 한데, 푸는 거 자체는 쉬운데?

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    N = int(input())
    tasks = [list(map(int, input().split())) for _ in range(N)]

    print(solve(tasks))
