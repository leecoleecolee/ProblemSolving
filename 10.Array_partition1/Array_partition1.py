from typing import *


class Solution:
    def Array_partition1(self, nums: List[int]) -> int:
        # 가장 큰 min 값 조합을 찾아라.
        # 우선 배열의 최대값은 같거나 그 다음으로 큰 값과 pair가 되어야하고,
        # 그 다음 큰 값에도 똑같이 진행된다.
        ret = 0

        nums.sort()
        while nums:
            ret += min(nums.pop(), nums.pop())
        return ret


if __name__ == "__main__":
    s = Solution()

    print(s.Array_partition1([]))
    print(s.Array_partition1([2, 2]))
    print(s.Array_partition1([1, 4, 3, 2]))
    print(s.Array_partition1([3, 2]))
