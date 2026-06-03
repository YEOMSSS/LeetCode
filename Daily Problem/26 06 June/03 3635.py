# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-03
# Problem Number : 3635

# -------------------------------

# [Problem] Earliest Finish Time for Land and Water Rides I

# 놀이기구가 2종이 있다. 육지 수상
# 각 놀이기구의 시간표가 주어진다. 시작시간과 지속시간.
# 둘 다 한번씩 탄 후의 최소 시각을 구하시오.
# 시간표의 길이는 둘 다 최대 50K개이다.


# [Intuition]

# 각각 5만개씩? 이러면 절대 브루트포스는 안된다.
# 뭔가 다른 방법을 찾아야 한다는 거지.

# 대상이 두개니까... 한쪽에 대해서 이분탐색이 가능하겠지.
# 지상을 탄 다음 탈 수 있는 물 중에서 가장 빨리 끝나는 걸 이분탐색으로 고를 수 있나?

# 하,,, 그냥 그리디로 풀면 안되는거임?
# 먼저 하는게 제일 빨리 끝난거에 그 다음 할수있는거중에 제일 빨리 끝나는거 고르자.
# 맞네. 얼마나 걸리는지는 페이크야... 그냥 가장 빨리 끝나는걸 고르면 돼.
# 쒸이벌, 그리디여도 그리디인걸 알아내기가 빡세...

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
    ) -> int:

        def func(s1, d1, s2, d2):
            # 첫 기구가 끝나는 가장 빠른 시각 구하기
            f1 = 1_000_000
            for i in range(len(s1)):
                f1 = min(f1, s1[i] + d1[i])
            # 첫 기구를 탄 후 두번째 기구를 끝낸 가장 빠른 시각 구하기
            f2 = 1_000_000
            for i in range(len(s2)):
                f2 = min(f2, max(f1, s2[i]) + d2[i])
            return f2

        land_to_water = func(landStartTime, landDuration, waterStartTime, waterDuration)
        water_to_land = func(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_to_water, water_to_land)


# -------------------------------

# [Summary]

# 그리디라는 사실을 깨닫는다면 빠르게 풀 수 있다.


# [Review]

# 깨닫기만 한다면 말이지.
