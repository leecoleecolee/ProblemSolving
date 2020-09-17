from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        l_idx, r_idx = 0, len(height) - 1
        left_max, right_max = height[l_idx], height[r_idx]

        while l_idx < r_idx:
            left_max, right_max = max(height[l_idx], left_max), max(
                height[r_idx], right_max)
            # move pointer higher
            if left_max <= right_max:
                volume += left_max - height[l_idx]
                l_idx += 1
            else:
                volume += right_max - height[r_idx]
                r_idx -= 1
        return volume


if __name__ == "__main__":
    s = Solution()
    li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    li2 = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.trapping_rain_water(li2))
