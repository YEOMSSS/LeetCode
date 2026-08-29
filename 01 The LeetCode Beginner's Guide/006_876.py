# -------------------------------

# Authored by : marigold2003
# Date : 2026-08-29
# Problem Number : 876

# -------------------------------

# [Problem] Middle of the Linked List

# 연결리스트 문제.
# head가 주어진다. 중간 노드를 반환해라.

# -------------------------------

# [LeetCode]

from typing import List, Optional

# -------------------------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 0
        curr = head

        while curr != None:
            curr = curr.next
            n += 1

        curr = head
        for _ in range(n // 2):
            if curr:
                curr = curr.next

        return curr

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # fast와 fast.next가 모두 None이 아닐 때만 루프를 돕니다.
        # 이 조건 덕분에 루프 내부에서 .next를 안전하게 사용할 수 있습니다.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # 두 칸 이동

        return slow


# -------------------------------

# [Summary]

# 두 수 앞을 보는 놈과 한 수 앞만 보는 두 개의 포인터를 같이 돌린다.
# 현재와 다음이 None이 아니면 fast는 두 칸 이동 가능하니까.


# [Review]

# 오, 투포인터를 이런 식으로도 쓸 수 있구나.
