from typing import *


class Solution:
    def trapping_rain_water(self, height: List[int]) -> int:
        # 스택을 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때, 그 격차만큼 물 높이를 채웁니다.
        # 스택에는 인덱스를 쌓습니다!

        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우,
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이를 처리합니다.
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume


if __name__ == "__main__":
    s = Solution()
    li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    li2 = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.trapping_rain_water(li))
