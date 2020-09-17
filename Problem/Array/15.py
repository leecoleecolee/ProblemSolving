from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        last = len(nums) - 1
        for i in range(last - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i, last
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, 4]))
