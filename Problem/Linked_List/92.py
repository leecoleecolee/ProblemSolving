from typing import *
from LinkedList import ListNode

class Solution:
        def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            if not head or m == n:
                return head

            root = start = ListNode(None)
            root.next = head
            
            print("root.val: {}".format(root.next.val))
                
            for _ in range(m - 1):
                start = start.next
            end = start.next
            
            for _ in range(n - m):
                tmp, start.next, end.next = start.next, end.next, end.next.next
                start.next.next = tmp
            return root.next
                
            
            

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    head = node5

    sol = Solution()
    sol.reverseBetween(head, 2, 4)
    while head is not None:
        print("head: {}".format(head.val))
        head = head.next
