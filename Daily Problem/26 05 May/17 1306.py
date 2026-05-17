# -------------------------------
# Link : https://leetcode.com/problems/jump-game-iii/description/?envType=daily-question&envId=2026-05-17
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-17
# Problem Number : 1306

# -------------------------------

# [Problem] Jump Game III

# 0과 자연수로 이루어진 리스트 arr이 들어온다.
# 인덱스 start에서 시작해서 인덱스값만큼 뒤나 앞으로 이동할 수 있다.
# 배열을 벗어날 수는 없으며, 값이 0인 인덱스에 도달할 수 있는지 판단하시오.


# [Intuition]

# 그래프다. bfs로 풀고 싶네.
# 벗어나지만 않으면 양옆으로 다 가고 visited에 추가하자.

# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import deque

# -------------------------------


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        N = len(arr)

        # 그래프를 만들지 않고 바로 진행

        queue = deque()
        visited = [False] * N

        queue.append(start)
        visited[start] = True

        while queue:
            curr = queue.popleft()

            if not arr[curr]:
                return True

            # 앞이나 뒤로 이동하기
            prev, nxt = curr - arr[curr], curr + arr[curr]

            if prev >= 0 and not visited[prev]:
                visited[prev] = True
                queue.append(prev)

            if nxt < N and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

        return False


# -------------------------------

# [Summary]

# bfs를 너무 오랜만에 짜서 헷갈렸다.
# 방문 후 visited를 추가하지 않는 실수를 했음.
# 굳이 graph를 만들지 않아도 돌아가는 문제였다.


# [Review]

# 슬슬 익숙한 놈들이 나오는구만.
# 이젠 그냥 사이트에서 푸는 것도 좀 익숙해졌다.
