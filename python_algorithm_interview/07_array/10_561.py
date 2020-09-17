# ---
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # ret = 0
        # nums.sort()

        # for num in nums[::2]:
        #     ret += num

        # return ret
        return sum(sorted(nums)[::2])

# ---
sol = Solution()
nums = [1,4,3,2]
print (sol.arrayPairSum(nums))