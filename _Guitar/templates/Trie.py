# 5월 21일 리트코드 문제 참고
# 알파벳 trie는 5월 28일 참고


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
