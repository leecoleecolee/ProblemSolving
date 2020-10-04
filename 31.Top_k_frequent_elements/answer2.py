from typing import *
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


if __name__ == "__main__":
    s = Solution()
    input = [1, 1, 1, 2, 2, 3]
    k = 2
    # input = [1]
    # k = 1
    print(s.topKFrequent(input, k))
