from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ---
        '''
        result = []
        curr_permute = []

        def dfs(element):
            if len(element) == 0:
                result.append(curr_permute[:])
            for e in element:
                remain_nums = element[:]
                remain_nums.remove(e)
                curr_permute.append(e)
                dfs(remain_nums)
                curr_permute.pop()

        dfs(nums)
        return result
        '''

        # ---
        result = []
        
        def dfs(nums, path):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                # dfs(nums[:i] + nums[i+1:], path.append(nums[i]))
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return result

sol = Solution()
nums = [1,2,3]
print (sol.permute(nums))