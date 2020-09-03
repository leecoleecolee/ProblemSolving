from typing import *
import collections


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        ret = collections.defaultdict(list)
        for word in strs:
            ret[''.join(sorted(word))].append(word)
        return ret.values()


if __name__ == "__main__":
    s = Solution()

    print(s.group_anagrams(["eat", "ate", "tea", "apple", "pleap"]))
