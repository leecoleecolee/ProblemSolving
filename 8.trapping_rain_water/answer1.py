from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        #  two pointer
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


if __name__ == "__main__":
    s = Solution()
    li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trapping_rain_water(li))
