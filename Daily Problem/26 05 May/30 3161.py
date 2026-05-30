# -------------------------------
# Link : https://leetcode.com/problems/block-placement-queries/description/?envType=daily-question&envId=2026-05-30
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-30
# Problem Number : 3161

# -------------------------------

# [Problem] Block Placement Queries

# 1로 시작하는 명령어가 오면 장애물을 설치한다.
# 2로 시작하는 명령어가 오면 0부터 현재까지 이 길이의 장애물을 설치할 수 있는지 판단한다.
# 판단 결과를 모은 리스트를 반환하시오. 쿼리는 150K개까지 입력된다.


# [Intuition]

# 흠... 장애물을 둬서 나눠질 때마다 그 나눠진 블럭의 길이를 저장해야하나.
# 그럼 나뉠때마다 어떤 식으로 저장해야하지?

# 일단 기록은 장애물만 기록하는 방식으로 할테고.
# 계속 장애물들이 정렬되어야 한다. 이거는 bisect로 할 수 있고...
# 그러면 앞뒤 차이를 계속 모아서 최댓값을 내야하는데, 이게 되나?

# -------------------------------

# [LeetCode]

from typing import List, Optional
from sortedcontainers import SortedList

# -------------------------------


class SegTree:
    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n * 2)

    def update(self, index: int, val: int):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])

    def query(self, index: int) -> int:
        index += self.n
        res = self.tree[index]
        while index > 1:
            if index % 2 == 1:
                res = max(res, self.tree[index - 1])
            index //= 2
        return res


# class Solution:
#     def getResults(self, queries: List[List[int]]) -> List[bool]:
#         Sorted = SortedList()
#         inter = SegTree(max(q[1] for q in queries))
#         res = []
#         Sorted.add(0)
#         inter.update(0, 0)
#         for q in queries:
#             if q[0] == 1:
#                 idx = Sorted.bisect(q[1])
#                 if idx < len(Sorted):
#                     nxt = Sorted[idx]
#                     inter.update(nxt, nxt - q[1])
#                 inter.update(q[1], q[1] - Sorted[idx - 1])
#                 Sorted.add(q[1])
#             else:
#                 prev = Sorted[Sorted.bisect(q[1]) - 1]
#                 mx = max(q[1] - prev, inter.query(prev))
#                 res.append(q[2] <= mx)
#         return res

# 왜자꾸 오류 표시가 나는거야? 그냥 주석처리해버려.


# -------------------------------

# [Summary]

# 세그먼트 트리와 이분 탐색을 사용한다.


# [Review]

# 뭐라는지 모르겠네...
