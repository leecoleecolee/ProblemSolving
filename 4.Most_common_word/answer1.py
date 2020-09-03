from typing import *
import re
import collections


# class Solution:
# def most_common_word(self, paragraph: str, banned: List[str]) -> List:
#     # Preprocessing - data cleansing
#     words = [word for word in re.sub(
#         r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

#     # Count word
#     counts = collections.Counter(words)
#     return counts.most_common(1)[0][0]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Preprocessing
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        # Count
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    s = Solution()
    # li = s.most_common_word("123 456 123 213421 123", ["a"])
    # print(li)
    li = s.mostCommonWord("123 456 123 213421 123", ["a"])
    print(li)
