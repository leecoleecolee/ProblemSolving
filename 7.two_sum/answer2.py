from typing import *


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return[seen[remaining], idx]
            seen[num] = idx
        return []


if __name__ == "__main__":
    s = Solution()
    nums = [3, 3]
    target = 6
    print(s.two_sum(nums, target))
