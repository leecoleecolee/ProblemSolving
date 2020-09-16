from typing import *
from LinkedList import ListNode

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    head = node5

    sol = Solution()
    sol.oddEvenList(head)
    while head is not None:
        print("head: {}".format(head.val))
        head = head.next

