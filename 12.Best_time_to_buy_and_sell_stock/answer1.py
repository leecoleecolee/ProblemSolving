from typing import List
import sys


class Solution:
    def myanswer(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.myanswer([7, 1, 5, 3, 6, 4]))
    print(s.myanswer([7, 5, 3, 2, 1]))
    print(s.myanswer([]))
    print(s.myanswer([1]))
