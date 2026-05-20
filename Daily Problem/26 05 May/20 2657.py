# -------------------------------
# Link : https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2026-05-20
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-20
# Problem Number : 2657

# -------------------------------

# [Problem] Find the Prefix Common Array of Two Arrays

# 1~N이 랜덤으로 배열된 두 순열이 입력된다.
# 인덱스 [i]까지 공통된 두 순열의 원소의 수를 list[i]에 입력한
# 리스트 list를 return하시오.


# [Intuition]

# 포인트는 뭐냐? 늘어난 두 칸만 비교하는거지.
# 전체의 교집합을 계속 검사하긴 힘들어.
# 각 칸을 set으로 관리하면서 계속 누적해주고,
# 한 칸씩 확인하면서 양칸에 더한 다음 상대칸에 내가 in이면 count에 +1.
# 만약 이번에 들어온 둘이 서로 같은거면 각각 +1하지말고 한번만 해주면 되겠네.


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        result = []

        Aset, Bset = set(), set()
        count = 0

        for i in range(len(A)):
            a, b = A[i], B[i]
            Aset.add(a)
            Bset.add(b)

            if a == b:
                count += 1

            else:
                if a in Bset:
                    count += 1
                if b in Aset:
                    count += 1

            result.append(count)

        return result


# -------------------------------

# [Summary]

# set을 이용해 in 관리를 쉽게 했다.
# 원소를 하나씩 관리하는 것도 포인트.
# 중복된 동작을 최대한 적게 해야 한다.


# [Review]

# 난이도 표시가 너무 적어가지고 미디엄 안에서도 편차가 엄청나구만.
