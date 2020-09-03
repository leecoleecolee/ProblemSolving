from typing import *


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.appen(nums[i], nums[left], nums[right])

                    # 중복인 수는 스킵
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results


if __name__ == "__main__":
    s = Solution()
    given_array = [-1, 0, 1, 2, -1, -4]
    # given_array = [-1, 1]
    print(s.three_sum(given_array))
