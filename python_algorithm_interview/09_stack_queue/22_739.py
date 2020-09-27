'''
* 문제
더 따뜻한 날씨를 위해 며칠을 기다려야 하는지 출력하라.
in) [73, 74, 75, 71, 69, 72, 76, 73]
out) [1, 1, 4, 2, 1, 1, 0, 0]
'''

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ...
        ret = [0] * len(T) # 리스트의 초기화
        stack = []

        for i, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                past = stack.pop()
                ret[past] = i - past
            stack.append(i)

        return ret