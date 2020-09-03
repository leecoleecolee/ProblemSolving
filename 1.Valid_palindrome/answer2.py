import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pretreatment
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # check palindrome
        while (len(strs) > 1):
            if strs.popleft() != strs.pop():
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    #s = "ab"
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))
