from typing import *
import collections

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse = None
        slow = fast = head

        # 런너를 활용하여 역순 리스트 만들기
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        # fast가 남아있다면 홀수개라는 뜻이다. 그럼 slow를 한칸 더 전진시켜서 가운데 값을 비껴나야한다.
        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next
        return not reverse


if __name__ == "__main__":
    s = Solution()
    input = ListNode(1)
    input.next = ListNode(2)
    input.next.next = ListNode(2)
    input.next.next.next = ListNode(1)
    print(s.isPalindrome(input))
