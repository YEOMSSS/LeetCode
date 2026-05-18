# -------------------------------
# Link : https://leetcode.com/problems/jump-game-iv/?envType=daily-question&envId=2026-05-18
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-18
# Problem Number : 1345

# -------------------------------

# [Problem] Jump Game IV

# 정수 배열 arr이 들어온다.
# i+1 또는 i-1로 이동 가능하다.
# 값이 동일한 칸으로 순간이동도 가능하다.
# 배열 밖으로 점프하는 건 불가능하다.
# 마지막 인덱스로 이동하기 위한 최소 단계 수를 반환하시오.

# 배열의 길이는 최대 50K이다.


# [Intuition]

# bfs네.
# 동일 칸의 인덱스만 기록하면 되겠다.
# defaultdict로 가자고.

# 근데, 동일 칸으로 다 이동해볼 필요가 있나?
# 어차피 최단거리 찾을거면 가장 목적지에 가깝게 텔포타야하는거같은데?
# 아니야, 의미는 있어. 뒤로 가거나 앞으로 가서 바로 목적지로 텔포될수도 있으니까.
# 여기서 내가 없애야 하는 건 연속되는 동일 수네. 이건 무조건 맨 끝으로 가면 된다.
# 아, 시작으로도. 연속된 묶음의 시작과 끝만 가보면 된다.

# 그런데, 결국 이건 연속된 부분을 없애지 못한다.
# 77777777은 해결되지만, 1717171717은 해결하지 못한다는 거임.
# 같은 값 그룹의 순회가 반복되며 시간초과가 생긴.

# 핵심은, 같은 값 순회는 한번이면 된다는 것이다.
# 이미 모든 칸에 텔포를 탔으니, 이후 텔포를 또 탈 필요가 없는 것.
# 매 칸마다 모든 칸에 텔포를 탈 이유가 전혀 없다는 게 포인트. 텔포경로 제거가 필요.

# [Approach]

# 1. defaultdict(list)로 동일 칸 기록하기. 이때 연속되는 경우 시작과 끝만 기록
# 2. bfs 돌려 최소횟수 찾기, 순간이동 한번 하면 동일 값의 순간이동장치 제거


# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import deque, defaultdict

# -------------------------------


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)

        can_move = defaultdict(set)

        for i, v in enumerate(arr):
            can_move[v].add(i)

        # print(can_move)

        queue = deque()
        visited = [False] * (N)

        queue.append(0)
        visited[0] = True

        count = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                # print(curr, count, queue)

                if curr == N - 1:
                    return count

                for nei in can_move[arr[curr]]:
                    if visited[nei]:
                        continue
                    queue.append(nei)
                    visited[nei] = True
                can_move[arr[curr]].clear()

                prev, nxt = curr - 1, curr + 1
                if prev >= 0 and not visited[prev]:
                    queue.append(prev)
                    visited[prev] = True
                if nxt < N and not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = True
            count += 1

        return count


# -------------------------------

# [Summary]

# 게으른 삭제. 이미 사용한 텔레포트를 다시 볼 필요가 없다.
# 이런 문제를 지난 번에 푼 적이 있는 것 같은데, 그새 잊었다.
# 다음에는 안까먹을듯. 무슨 느낌인지 알겠다.


# [Review]

# 확실히 문제가 질이 좋긴 함.
