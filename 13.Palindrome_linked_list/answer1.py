from typing import *
import collections

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:


if __name__ == "__main__":
    s = Solution()
    input = ListNode(1)
    input.next = ListNode(2)
    input.next.next = ListNode(2)
    input.next.next.next = ListNode(1)
    print(s.isPalindrome(input))
