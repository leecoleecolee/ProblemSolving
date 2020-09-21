from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 두 값을 리스트의 val을 비교한 다음에 큰 값을 오른쪽으로, 작은 값을 왼쪽으로 옮기고 왼쪽 리스트를 반환.
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1이 마지막 노드이거나, l2가 있는데 l1의 val이 l2의 val보다 큰 경우
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


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
