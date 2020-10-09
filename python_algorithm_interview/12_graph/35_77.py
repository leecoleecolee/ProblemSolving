from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(element, start, k):
            if k == 0:
                result.append(element[:])
            for i in range(start, n + 1):
                element.append(i)
                dfs(element, i + 1, k - 1)
                element.pop()
            
        dfs([], 1, k)
        return result

sol = Solution()
n = 4
k = 2
print (sol.combine(n, k))