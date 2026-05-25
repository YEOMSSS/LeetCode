# -------------------------------
# Link : https://leetcode.com/problems/jump-game-v/description/?envType=daily-question&envId=2026-05-24
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-24
# Problem Number : 1340

# -------------------------------

# [Problem] Jump Game V

# 우선 점프는 더 작은 쪽으로만 이동이 가능하다.
# 점프 목표까지의 모든 값들이 다 자신보다 작아야 한다.
# 이동은 앞뒤로 최대 d만큼 할 수 있으며, 배열을 벗어날 수는 없다.
# 방문할 수 있는 인덱스의 수를 반환하시오.


# [Intuition]

# 존나 어려워서 솔루션 봤다.
# 아니 뭔 씨발, dfsR + dp는 뭐야

# 발상은 이렇다.
# 어쨌든 최종 도착 칸들은 다 정해져 있을거 아니야?
# 걔들에서부터 하나씩 올라간다는 느낌으로 하는거지.
# 그래서 재귀를 사용한다.

# 그리고 같은 경로를 계속 사용할 거니까, dp를 여기 얹는다.
# 어차피 경로 상에 있는 모든 원소의 경로는 겹치게 된다는 걸 알아야 한다.


# -------------------------------

# [LeetCode]

from typing import List, Optional
from functools import cache

# -------------------------------


class Solution:
    # dp list version
    def maxJumpsDP(self, arr: List[int], d: int) -> int:
        N = len(arr)

        # dp[pos]에는 현재 인덱스에서의 최대방문가능인덱스수가 저장된다.
        dp = [0] * N

        def dfsR(pos):
            # 이미 경로 제작이 완료되었다면 패스
            if dp[pos]:
                return
            # 현재 칸이 최종 도달 경로라면 최소횟수인 1이 된다.
            dp[pos] = 1

            # 이동할 경로는 i로 한다.

            # pos - 1 ~ pos - d를 검사한다.
            i = pos - 1
            # 배열을 넘어갈 수 없으며, pos-i는 d이고, 더 높은 벽을 만나면 멈춰야 한다.
            while i >= 0 and pos - i <= d and arr[i] < arr[pos]:
                # 이동한 경로에서 dfs를 돌려 최종 경로부터 쌓아올린다.
                dfsR(i)
                dp[pos] = max(dp[pos], dp[i] + 1)
                i -= 1

            # pos + 1 ~ pos + d를 검사한다.
            i = pos + 1
            # 배열을 넘어갈 수 없으며, i-pos는 d이고, 더 높은 벽을 만나면 멈춰야 한다.
            while i < N and i - pos <= d and arr[i] < arr[pos]:
                dfsR(i)
                dp[pos] = max(dp[pos], dp[i] + 1)
                i += 1

        for i in range(N):
            dfsR(i)

        result = max(dp)
        return result

    # @cache version
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)

        # @cache가 이미 사용한 dfsR(pos)의 return 값을 저장해 준다.
        @cache
        def dfsR(pos):
            # 최소 반환값은 자신인 1이다.
            best = 1

            # 이동할 경로는 i로 한다.

            # pos - 1 ~ pos - d를 검사한다.
            i = pos - 1
            # 배열을 넘어갈 수 없으며, pos-i는 d이고, 더 높은 벽을 만나면 멈춰야 한다.
            while i >= 0 and pos - i <= d and arr[i] < arr[pos]:
                # 이동한 경로에서 dfs를 돌려 최종 경로부터 쌓아올린다.
                best = max(best, dfsR(i) + 1)
                i -= 1

            # pos + 1 ~ pos + d를 검사한다.
            i = pos + 1
            # 배열을 넘어갈 수 없으며, i-pos는 d이고, 더 높은 벽을 만나면 멈춰야 한다.
            while i < N and i - pos <= d and arr[i] < arr[pos]:
                best = max(best, dfsR(i) + 1)
                i += 1

            # 이동이 완료된 서브트리값을 반환한다.
            return best

        # 모든 값에서 시작하며 result를 갱신한다.
        result = 1
        for i in range(N):
            result = max(result, dfsR(i))

        return result


# -------------------------------

# [Summary]

# 재귀 dfs를 곁들인 dp. DAG를 어떻게 해결할 것인가?
# 재귀에 대한 이해력이 높아지는 기분이 든다.
# @cache를 이용해 dfsR을 더 깔끔한 탑다운 dp로 풀 수 있었다.


# [Review]

# dp의 세계도 존나게 깊네 진짜.
# 재귀는 거꾸로 올라갈 때 편하다. 이걸 항상 기억하고 잘 사용하자.
