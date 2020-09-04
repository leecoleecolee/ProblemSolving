from typing import List


class Solution:
    def myanswer(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        profit = []
        for i in range(len(prices) - 1):
            profit.append(max(prices[i+1:]) - prices[i])
        ret = max(profit)
        ret = 0 if ret < 0 else ret
        return ret


if __name__ == "__main__":
    s = Solution()
    # print(s.myanswer([7, 1, 5, 3, 6, 4]))
    # print(s.myanswer([7, 5, 3, 2, 1]))
    # print(s.myanswer([]))
    print(s.myanswer([1]))
