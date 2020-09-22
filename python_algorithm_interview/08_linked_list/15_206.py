'''
* 문제
연결리스트를 뒤집어라.
in) 1->2->3->NULL
out) 3->2->1->NULL

* 풀이방법
1) 재귀
2) 반복

* [x] 1회차
기본적인 문제임에도 연결리스트나 재귀 등에 대한 이해가 부족해서 아직 스스로 풀기가 어려웠다.
하지만 이해에 도움이 되는 굉장히 좋은 문제.

* [ ] 2회차
'''

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