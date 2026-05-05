# -------------------------------
# Link : https://leetcode.com/problems/rotate-list/?envType=daily-question&envId=2026-05-05
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-05
# Problem Number : 61


# [Problem] Rotate List

# 연결 리스트가 입력된다.
# 가장 안쪽의 노드를 head로 올리는 연산을 k회 반복하시오.
# k는 2*10**9로 매우 크다. 노드는 500개까지 주어진다.
# 연산을 완료한 연결 리스트를 반환하시오.


# [Intuition]

# k를 노드 개수로 나눌 필요가 있다.
# 우선 끝까지 탐색해서 길이를 구해야 한다.
# 이게 입력이 어떤 식으로 들어오는지를 몰라서 vsc로 하기가 애매하다.
# 그냥 사이트 안에서 풀어야 할 듯.

# 그리고 다 꺼내서 deque에 저장하고
# rotate로 모양 만든다음에 popleft로 꺼내서
# 새로운 head를 하나 만들자.

# -------------------------------
# [LeetCode]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------


from collections import deque


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        count = 0
        vals = deque()

        curr = head
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
            count += 1

        k %= count
        vals.rotate(k)

        newhead = ListNode(vals.popleft())
        temp = newhead
        while vals:
            temp.next = ListNode(vals.popleft())
            temp = temp.next

        return newhead


# -------------------------------

# [Summary]

# 잘 굴러간다.
# 실제로 연결 리스트로 문제를 풀어본 건 처음이다.


# [Review]

# 그냥 사이트에서 푸는 게 생각보다 편하네?
# 사이트에서 풀고 저장만 vsc로 하는 것도 고려해볼만 한 듯.
# 자동완성이 안 되는데도 푸는 날 보니 고수가 된 기분이다.

# -------------------------------
# -------------------------------
