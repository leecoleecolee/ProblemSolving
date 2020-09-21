from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 왼쪽 노드의 next를 prev값을 넣는다.
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
