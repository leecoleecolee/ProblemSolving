import string
import collections


class Solution:
        def removeDuplicateLetters(self, s: str) -> str:
            counter = collections.Counter(s)
            print(counter)

if __name__ == "__main__":
    sol = Solution();
    print(sol.removeDuplicateLetters('asf'))

