'''
* 문제
연결리스트에서 페어끼리 스왑하는 문제.
in) 1->2->3->4->5->6
out) 2->1->4->3->6->5

* 풀이방법
1) 반복
2) 재귀

* [x] 1회차
아직 스스로 풀이하는 것은 어려우나, 연결리스트와 스왑, 반복과 재귀를 이해하는 데에 아주 적절한 문제.

* [ ] 2회차
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # --- 반복
        # root = prev = ListNode(None)
        # prev.next = head

        # while head and head.next:
        #     b = head.next
        #     head.next = b.next
        #     b.next = head

        #     prev.next = b
        #     head = head.next
        #     prev = prev.next.next

        # return root.next

        # --- 재귀
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head