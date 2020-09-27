from typing import *


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = []
        day = []

        for i, te in enumerate(T):
            while stack and te > stack[-1]:
                stack.pop()
                idx = day.pop()
                ret[idx] = i - idx
            stack.append(te)
            day.append(i)

        return ret


if __name__ == "__main__":
    s = Solution()
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(input))
