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

        # 아래처럼 코딩하면 while문에서 무한루프에 걸린다. odd와 cur가 같은 Node를 가리키는 상태에서 odd.next = cur하여 자기자신을 가리키게 되기 때문이다.
        # ret = ListNode(None)
        # ret.next = cur = odd = head
        # 아래처럼 구현하자. Thanks to gmoon.
        ret = cur = ListNode(None, head)
        odd = head
        even_head = even = head.next

        i = 1
        while cur:
            if i % 2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            i += 1
        even.next = None
        odd.next = even_head
        return ret.next


if __name__ == "__main__":
    s = Solution()
    nodes = ListNode(None)
    print(s.answer1(nodes))
