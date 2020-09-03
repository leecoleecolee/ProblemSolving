from typing import *


class Solution:
    def longest_palindromic_substring(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s


if __name__ == "__main__":
    s = Solution()
    print(s.longest_palindromic_substring("babad"))
