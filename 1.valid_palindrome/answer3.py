import re
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링!
        s = re.sub('[^a-z0-9]', '', s)

        # 아님 아래처럼 해도 된다.
        # p = re.compile('[a-z0-9]')
        # s = p.findall(s)

        return s == s[::-1]


if __name__ == "__main__":
    a = Solution()
    #s = "ab"
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))
