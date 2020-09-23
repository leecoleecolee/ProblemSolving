# Definition for singly-linked list.
from typing import ListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd_root = odd = head
        even_root = even = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_root
        return odd_root


if __name__ == "__main__":
    s = Solution()
    nodes = ListNode(None)
    print(s.answer1(nodes))
