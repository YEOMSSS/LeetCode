# -------------------------------
# Link : https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/?envType=daily-question&envId=2026-05-27
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-27
# Problem Number : 3121

# -------------------------------

# [Problem] Count the Number of Special Characters II

# string에 대문자와 소문자가 모두 나타나는 알파벳은 특수하다.
# 추가로 모든 소문자가 첫 번째 대문자가 나타나기 이전에 등장한다면 더 특수하다.
# 더 특수한 알파벳이 몇 가지 있는지 반환하시오.


# [Intuition]

# 배열을 하나만 만드는 게 더 편할지도 모르겠다는 생각이 든다.
# 앞에서부터 순서대로 훑는다고 생각할 때 뭘 체크해야 하지?


# [Approach]

# 1. 등장하지 않은 알파벳이 대문차로 처음 등장하면 실패.
#    더 특수하기 위해서는 반드시 소문자로 알파벳이 처음 등장해야 한다.
# 2. 대문자 뒤에 소문자가 등장하면 실패.
#    더 특수하기 위해서는 모든 소문자가 대문자 이전에 등장해야 한다.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


# 65~90, 97~122
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        N = len(word)
        # 0 등장안함, 1 대문자, 2 소문자, 3 실패
        arr = [0] * 26

        for ch in word:
            CH = ord(ch)

            # 대문자인 경우
            if CH <= 90:
                if arr[CH - 65] == 3:
                    continue

                # 등장하지 않은 알파벳이면 실패
                if arr[CH - 65] == 0:
                    arr[CH - 65] = 3
                # 나머지 경우는 대문자 등장 표시
                else:
                    arr[CH - 65] = 1

            # 소문자인 경우
            else:
                if arr[CH - 97] == 3:
                    continue

                # 대문자가 등장했었다면 실패
                if arr[CH - 97] == 1:
                    arr[CH - 97] = 3
                # 나머지 경우는 소문자 등장 표시
                else:
                    arr[CH - 97] = 2

        # 1로 남아있는 요소가 성공한 알파벳이다.
        count = arr.count(1)
        return count


# -------------------------------

# [Summary]

# 애드혹이라고 해야 할까? 구현 관리하는법.

# [Review]

# 이번 시리즈는 특수한 숫자 찾기인가보네. 이번주도 즐겁겠구만.
