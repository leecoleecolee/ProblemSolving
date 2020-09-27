from typing import *


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


if __name__ == "__main__":
    s = Solution()
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(input))
