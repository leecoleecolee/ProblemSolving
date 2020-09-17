from typing import *


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            our_target = target - num
            if our_target in seen:
                return [seen[our_target], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    s = Solution()
    nums = [1, 8, 2, 3, 5]
    target = 6
    print(s.two_sum(nums, target))
