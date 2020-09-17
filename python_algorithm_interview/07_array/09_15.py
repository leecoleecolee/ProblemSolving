# ---
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        # for i in range(len(nums) - 2): # 브루트포스
        #     if 0 < i and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, len(nums) - 1):
        #         if i + 1 < j and nums[j] == nums[j - 1]:
        #             continue
        #         for k in range(j + 1, len(nums)):
        #             if j + 1 < k and nums[k] == nums[k - 1]:
        #                 continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.append([nums[i], nums[j], nums[k]])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                # if [nums[i], nums[left], nums[right]] not in result:
                #         result.append([nums[i], nums[left], nums[right]])
                #     left += 1
                #     right -= 1
                    result.append([nums[i], nums[left], nums[right]])
                    # while nums[left] == nums[left + 1] and left < right:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while nums[right] == nums[right - 1] and left < right:
                        right -= 1
                    left += 1
                    right -= 1

        return result

# ---
sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print (sol.threeSum(nums))