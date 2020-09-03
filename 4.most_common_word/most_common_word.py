from typing import *
import re
import collections


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str
    # Preprocessing - data cleansing
    words = [word for word in re.sub(
        r'^\w', ' ', paragraph).lower().split() if word not in banned]

    # Count word
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=count.get)
