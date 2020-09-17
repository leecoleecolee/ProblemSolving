from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height(right)

        while left <= right:
            left_max, right_max = max(left_max, height[left]), max(
                right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]


if __name__ == "__main__":
    s = Solution()
    li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    li2 = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.trapping_rain_water(li))
