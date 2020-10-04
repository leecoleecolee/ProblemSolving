import collections
from typing import List
import heapq

# --- Counter과 heapq를 이용한 방법
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        count_heap = [] # 최소 힙

        for c in count:
            heapq.heappush(count_heap, (-count[c], c))

        # # 문제 잘못 이해. k번 이상 등장하는 건줄... 아마 상위 k개만 추출하는게 맞을 것.
        # ret = []
        # for c in count_heap:
        #     tmp = heapq.heappop(count_heap)
        #     if tmp[0] * -1 < k:
        #         break
        #     ret.append(tmp[1])
        
        ret = []
        for _ in range(k):
            # # 조건에 1 ≤ k ≤ number of unique elements 가 있어서 안해줘도 됨.
            # if not count_heap:
            #     break
            ret.append(heapq.heappop(count_heap)[1])

        return ret
'''

# --- Counter 메서드와 zip을 이용한 방법
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return list(zip(*count.most_common(k)))[0]

# ---
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print (sol.topKFrequent(nums, k))