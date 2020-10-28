class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # --- 알고리즘: 투포인터 (60ms / 14.4MB)
        # left, right = 0, len(numbers) - 1
        # while left != right:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         return [left + 1, right + 1]
        # return []

        # --- 알고리즘: 이진 검색 (60ms / 14.5MB)
        for i, num in enumerate(numbers):
            wanted = target - num
            i2 = bisect.bisect_left(numbers, wanted, lo = i + 1)
            if i2 < len(numbers) and numbers[i2] == wanted:
                return [i + 1, i2 + 1]