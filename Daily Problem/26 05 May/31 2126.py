# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-31
# Problem Number : 2126

# -------------------------------

# [Problem] Destroying Asteroids

# 자신보다 작거나 같은 것을 먹고 합쳐지면 서로 더해진다.
# 전부 삼킬 수 있는지 판정하시오.


# [Intuition]

# 숫자 합치기 게임이구만. 정렬하고 그리디로 하면 되는거 아님?

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for n in asteroids:
            if mass < n:
                return False
            mass += n

        return True


# -------------------------------

# [Summary]

# 무조건 작은거부터 먹으면 된다.


# [Review]

# 근데 좀 더 좋은 방법이 있으니까 이 문제가 미디엄인거겠지?
