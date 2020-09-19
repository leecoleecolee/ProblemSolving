from typing import *
import collections


# 조건1. 시간 복잡도는  O(N)
# 조건2. 나누기를 하지마라.

class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            forward, backward = collections.deque(), collections.deque()
            f = 1
            b = 1
            _len = len(nums)
            for i in range(_len):
                forward.append(f)
                backward.appendleft(b)
                f *= nums[i]
                b *= nums[_len - i - 1]
            return [a*b for a, b in zip(forward, backward)]
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))

