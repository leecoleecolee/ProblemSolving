from typing import List
import sys # sys.maxsize

# ---
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # buy = prices[0] # sys.maxsize 를 몰라서 첫값으로 하느라 예외처리까지 추가됨.

        buy = sys.maxsize # 위와 로직은 같다

        ret = 0

        for price in prices:
            buy = min(buy, price)
            ret = max(ret, price - buy)
        return ret

# ---
sol = Solution()
prices = [7,1,5,3,6,4]
print (sol.maxProfit(prices))