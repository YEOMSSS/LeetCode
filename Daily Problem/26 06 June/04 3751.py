# -------------------------------

# Authored by : marigold2003
# Date : 2026-06-04
# Problem Number : 3751

# -------------------------------

# [Problem] Total Waviness of Numbers in Range I

# 어떤 수를 자릿수마다 확인할 때, 양쪽이 가운데보다 크면 골짜기가 생긴다.
# 반대로, 양쪽이 가운데보다 작으면 피크가 생긴다.
# num1~num2 사이 모든 수에서 생기는 골짜기와 피크의 총합을 반환하시오.


# [Intuition]

# 121은 피크고 123은 경사네.
# 1321은 피크 한번 골짜기 한번.
# 13131은 2피크 1골짜기... 이걸 모든 수에 대해 해야하나?
# 그냥 간단하게 브루트포스로 될거같기도하고... 100K정도면

# 근데 dp로 풀 수 있을거라는 느낌이 오긴 한다.
# 워낙 수끼리 겹치는 부분이 많으니.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0

        for n in range(max(100, num1), num2 + 1):
            num_list = list(map(int, str(n)))
            for i in range(1, len(num_list) - 1):
                if num_list[i - 1] <= num_list[i] <= num_list[i + 1]:
                    continue
                if num_list[i - 1] >= num_list[i] >= num_list[i + 1]:
                    continue
                print(num_list)
                res += 1

        return res


# -------------------------------

# [Summary]

# list(map(int, str(num)))으로 자릿수별로 분해해서 사용했다.


# [Review]

# 간단하게 풀 수 있었으나, 너무나도 비효율적인 방법임.
