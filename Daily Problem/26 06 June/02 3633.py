# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-02
# Problem Number : 3633

# -------------------------------

# [Problem] Earliest Finish Time for Land and Water Rides I

# 놀이기구가 2종이 있다. 육지 수상
# 각 놀이기구의 시간표가 주어진다. 시작시간과 지속시간.
# 둘 다 한번씩 탄 후의 최소 시각을 구하시오.
# 시간표의 길이는 둘 다 최대 100개이다.


# [Intuition]

# 이 백준스러운 비문학은 뭐냐?
# 그냥 브루트포스 할련다.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int | float:

        res = float("inf")
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                cur = landStartTime[i] + landDuration[i]
                if cur < waterStartTime[j]:
                    cur = waterStartTime[j]
                cur += waterDuration[j]
                res = min(res, cur)

                cur = waterStartTime[j] + waterDuration[j]
                if cur < landStartTime[i]:
                    cur = landStartTime[i]
                cur += landDuration[i]
                res = min(res, cur)

        return res


# -------------------------------

# [Summary]

# 일단 브루트포스로 풀었다.
# 시리즈물인걸 보니 아마 더 어려워질듯.


# [Review]

# 요즘 왜 이렇게 뭘 하기가 싫을까... 이러면 안되는데.
# 의지박약이 왔나? 시험기간이 다가와서 그런가?
