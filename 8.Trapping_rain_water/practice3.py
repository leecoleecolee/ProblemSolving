from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume


if __name__ == "__main__":
    s = Solution()
    li = [0, 1, 0, 2, 0, 0, 1, 3, 2, 1, 2, 1]
    li2 = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.trapping_rain_water(li))
