from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy_head = ListNode(None)

        # Both l1 and l2 still have elements
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # if l2 is empty, directly merge l1, else if l1 is empty, directly merge l2
        cur.next = l1 or l2

        # return the head of merged sorted linked list
        return dummy_head.next


if __name__ == "__main__":
    s = Solution()
    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = ListNode(6)

    input2 = ListNode(1)
    input2.next = ListNode(3)
    input2.next.next = ListNode(4)

    res = s.mergeTwoLists(input1, input2)
    while res is not None:
        print(res.val)
        res = res.next
