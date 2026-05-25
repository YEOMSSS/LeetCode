# -------------------------------
# Link : https://leetcode.com/problems/jump-game-vii/?envType=daily-question&envId=2026-05-25
# https://leetcode.com/problems/jump-game-vii/editorial/comments/3446129/ 사용 풀이, 나의 답글
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-25
# Problem Number : 1871

# -------------------------------

# [Problem] Jump Game VII

# 처음에 맨앞 '0'에 서있고, 다른 '0'으로만 이동할 수 있다.
# 최소점프만큼은 이동해야하고, 최대점프보다 적게 이동해야한다.
# 문자열을 넘어갈 수는 없다... 까지. 그리고 이동은 오른쪽으로만이네.
# 도달 횟수같은거 없이, 그냥 도달 가능 여부만 확인하면 된다.


# [Intuition]

# 깨달아 버린 거야... 이거 가장 오른쪽에 있는 텔포 타는 문제잖아!!
# 현재 인덱스 + maxjump에서 현재 인덱스 + minjump로 내려가면서
# 새로운 0이 있는지 확인하면 되겠다.
# 이런 식으로 하면 본 걸 또 볼 일은 없어. 실패 시 좀 반복되는거만 빼면 뭐...

# 어!!! minjump가 존재하기 때문에 가장 작은 0으로 뛰어야하나?
# 어떤 0으로 텔레포트를 타는게 최적의 수지? 그냥 텔포가 아니었네 이거.
# 다 타봐야겠는데? dp계열 문제였잖아... 범위 작으니까 그래프 완탐 되나?

# 이 씨벌 그냥 그래프로 하면 안되나??
# 와... visited 안만들고 할 수 있구나. 이러면 얘기가 다르지. O(n)이라니...


# -------------------------------

# [LeetCode]

from typing import List, Optional
from collections import deque

# -------------------------------


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        N = len(s)
        arr = list(map(int, s))

        queue = deque()
        # visited = []
        # 와, visited를 안만들어버리네?
        checked = 0
        queue.append(0)

        while queue:
            curr = queue.popleft()

            if curr == N - 1:
                return True

            for i in range(
                max(checked + 1, curr + minJump), min(curr + maxJump + 1, N)
            ):
                if arr[i]:
                    continue
                queue.append(i)

            checked = curr + maxJump

        return False


# -------------------------------

# [Summary]

# 더 줄이기 위한 노력을 한다.
# 앞으로만 가면 되는 거잖아, 그러면 visited를 굳이 만들어야 할까? 와...


# [Review]

# 남이 쓴 코드를 읽는 건 정말 도움이 많이 되는구나.
