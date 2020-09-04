from typing import *


class Solution:
    def answer2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for n in nums:
            if n % 2 == 0:
                sum += n
        return sum
