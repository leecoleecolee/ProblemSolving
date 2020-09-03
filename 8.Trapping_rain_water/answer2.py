from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        # stack
        stack = []
        volume = 0

        for i in range(len(height)):
            # 현재 높이가 이전 높이보다 높은 인덱스라면
            while stack and height[i] > height[stack[-1]]:

                # 스택에서 꺼낸다.
                prev_top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[prev_top]
                volume += distance * waters

            stack.append(i)
        return volume


if __name__ == "__main__":
    s = Solution()
    # li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    li = [2, 0, 0, 2]
    print(s.trapping_rain_water(li))
