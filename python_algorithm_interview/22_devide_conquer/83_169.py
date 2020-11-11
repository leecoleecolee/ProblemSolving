class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # --- 정렬을 이용한 방법 --- #
        nums.sort()
        return nums[len(nums) // 2]