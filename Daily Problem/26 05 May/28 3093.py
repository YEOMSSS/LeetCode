# -------------------------------
# Link : https://leetcode.com/problems/longest-common-suffix-queries/description/?envType=daily-question&envId=2026-05-28
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-28
# Problem Number : 3093

# -------------------------------

# [Problem] Longest Common Suffix Queries

# 단어가 담긴 배열과 단어 쿼리가 담긴 배열이 들어온다.
# 단어 쿼리 배열에 담긴 모든 단어를 단어가 담긴 배열에 비교하며
# 가장 긴 공통 접미사를 가진 단어의 인덱스를 모아 반환하시오.


# [Intuition]

# 5월 21일에 접두사로 풀었던 문제. 그때 아마 트라이를 사용했지?
# 이 문제도 그냥 단어를 다시 뒤집기만 하면 접두사 문제랑 똑같아진다.
# 근데 여기서는 단어의 인덱스를 찾는 것까지 해야 한다는 게 차이점.
# 그러면 트라이 내부에 정보를 저장해야할 필요가 있다.

# 음, 근데 단어가 가장 짧은 걸 출력해야 한다는 게 좀 어렵네.


# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


class TrieNode:
    def __init__(self):
        # # 소문자 26개
        self.children: list = [None] * 26
        # self.children = dict()

        # 짧은 단어부터 뽑아내기 위한 변수들
        self.minlen = float("inf")
        self.idx = float("inf")


# 트라이를 만들자.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 트라이에 값을 저장하자.
    def insert(self, word, wid):
        node: TrieNode = self.root
        wlen = len(word)

        # 먼저 들어온게 우선이니까 등호는 없어도 된다.
        if wlen < node.minlen:
            node.minlen = wlen
            node.idx = wid

        # 각 char에 대해 확인한다.
        for ch in word:
            idx = ord(ch) - 97

            # 현재 위치에 노드가 없으면 하나 만들어준다.
            # if idx not in node.children:
            if not node.children[idx]:
                node.children[idx] = TrieNode()

            # 한 칸 내려가자.
            node = node.children[idx]

            if wlen < node.minlen:
                node.minlen = wlen
                node.idx = wid

    # 가장 긴 접미사를 가진 가장 짧은 단어의 인덱스 반환
    def query(self, word):
        # 루트부터 확인하며 내려간다.
        node = self.root

        for ch in word:
            idx = ord(ch) - 97

            # 현위치에 노드가 있으면 길이를 늘리고, 타고 내려간다.
            if node.children[idx]:
                node = node.children[idx]

            # 없으면 탐색을 멈춘다.
            else:
                break

        return node.idx


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:

        trie = Trie()

        for idx, word in enumerate(wordsContainer):
            trie.insert(word[::-1], idx)

        result = []
        for word in wordsQuery:
            result.append(trie.query(word[::-1]))

        return result


# -------------------------------

# [Summary]

# 트라이 응용하기.
# 트라이의 끝까지 도달하지 않고 단어의 중간 경로에서 멈춰도
# 현재 어떤 단어 위를 달리고 있는지 저장한다.
# 현재 트라이노드의 저장된 가장 짧은 단어의 인덱스를 비교하며 삽입한다.


# [Review]

# 트라이도 응용하기 나름이구나.
# 진짜 괜찮은 자료구조긴 하네.
# 트라이노드에 children을 딕셔너리로 만드는 것도 좋아보이긴 한다.
