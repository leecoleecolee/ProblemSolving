from typing import *
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        set_nums = set(nums)
        ret = []

        for i in set_nums:
            if cnt[i] >= k:
                ret.append(i)

        return ret


if __name__ == "__main__":
    s = Solution()
    input = [1, 1, 1, 2, 2, 3]
    k = 2
    input = [1]
    k = 1
    print(s.topKFrequent(input, k))


# failed
# input[1, 2]
# k = 2
