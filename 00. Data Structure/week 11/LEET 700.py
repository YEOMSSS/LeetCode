# -------------------------------
# Link : https://leetcode.com/problems/search-in-a-binary-search-tree/
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-13
# Problem Number : 700

# -------------------------------

# [Problem] Search in a Binary Search Tree

# 어느 BST의 root와 탐색목표노드인 val이 주어진다.
# 탐색목표노드를 root로 하는 서브트리의 root를 반환하시오.
# 만약 존재하지 않는다면 None을 반환한다.


# [Intuition]

# BST니까 크면 오른쪽 작으면 왼쪽으로 가면 된다.
# 목표에 도착하거나, 탐색을 실패할 때까지 반복하면 된다.


# -------------------------------
# [LeetCode]
# -------------------------------


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode | None:

        curr = root
        while curr != None and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr


# -------------------------------

# [Summary]

# None은 TreeNode가 아님에 주의.
# 목표 TreeNode에 도달하기만 해도 그 자체가 답이 된다.


# [Review]

# 배운 대로 적용하면 된다.
