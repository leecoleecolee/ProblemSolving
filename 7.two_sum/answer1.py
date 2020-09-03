from typing import *


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            retarget = target - num
            if retarget in nums[idx+1:]:
                idx2 = nums[idx+1:].index(retarget) + idx+1
                return idx, idx2


if __name__ == "__main__":
    s = Solution()
    nums = [3, 3]
    target = 6
    print(s.two_sum(nums, target))
