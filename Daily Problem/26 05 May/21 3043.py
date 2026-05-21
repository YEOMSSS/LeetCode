# -------------------------------
# Link : https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2026-05-21
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-21
# Problem Number : 3043

# -------------------------------

# [Problem] Find the Length of the Longest Common Prefix

# 두 정수 배열이 주어진다.
# 각 배열에서 정수를 하나씩 뽑는다.
# 뽑은 정수를 앞에서부터 비교해서 겹치는 부분을 센다.
# 겹치는 접두사의 길이가 가장 긴 경우의 길이를 반환하시오.


# [Intuition]

# 이거 트라이다. 드디어 트라이를 사용해 보나? 긴장이 되는군.
# 이렇게 정수 탐색할 때는 10칸만 만들면 되니까 확실히 트라이가 좋다.

# 10칸짜리 리스트를 노드로 해가지고, 계속 타고 들어가도록 하자.
# 원래 마지막에 값을 저장하던가? 근데 이건 값을 알 필요 없으니 패스.
# 그냥 어느 깊이까지 존재하는지만 확인하자.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class TrieNode:
    def __init__(self):
        # 숫자는 10개다. 0123456789
        self.children: list = [None] * 10


# 트라이를 만들자.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 트라이에 값을 저장하자.
    def insert(self, num):
        node = self.root

        num_str = str(num)
        # 각 자릿수에 대해 확인한다.
        for digit in num_str:
            idx = int(digit)

            # 현재 위치에 노드가 없으면 하나 만들어준다.
            if not node.children[idx]:
                node.children[idx] = TrieNode()

            # 한 칸 내려가자.
            node = node.children[idx]

    # 일치할 때까지 내려가서 그 길이를 반환한다.
    def find_longest_prefix(self, num):
        # 루트부터 확인하며 내려간다.
        node = self.root

        length = 0
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)

            # 현위치에 노드가 있으면 길이를 늘리고, 타고 내려간다.
            if node.children[idx]:
                length += 1
                node = node.children[idx]

            # 없으면 탐색을 멈춘다.
            else:
                break

        return length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        # 배열1을 트라이에 전부 저장한다.
        for num in arr1:
            trie.insert(num)

        longest_prefix = 0

        # 배열2를 트라이에 전부 탐색한다.
        for num in arr2:
            length = trie.find_longest_prefix(num)
            # 최댓값으로 갱신하면 된다.
            longest_prefix = max(longest_prefix, length)

        return longest_prefix


# -------------------------------

# [Summary]

# 트라이를 사용한 삽입과 검색.
# 매우 교육적인 문제다.


# [Review]

# 백준이랑은 확실히 다른 맛...
# 랜덤 마라톤과는 격이 다르다.
