# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # --- 재귀
        def reverse(curr, prev):
            if not curr:
                return prev
            next, curr.next = curr.next, prev
            return reverse(next, curr)
        return reverse(head, None)

        # --- 반복
        # curr = head
        # prev = None
        # while curr:
        #     next, curr.next = curr.next, prev
        #     prev, curr = curr, next
        # return prev

# ---
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
ret = sol.reverseList(head)

while ret:
    print(ret.val)
    ret = ret.next