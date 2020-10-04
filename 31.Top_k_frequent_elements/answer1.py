from typing import *
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # 빈도 수를 키값으로 하여 힙에 저장. 이 때 최소 힙임을 감안하여 빈도 수에 음수를 곱하여 저장한다. 결과적으로 가장 큰 빈도 수가 가장 높은 우선순위를 가지게 하기 위해서이다.
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        # k번 만큼 힙에서 추출.
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


if __name__ == "__main__":
    s = Solution()
    input = [1, 1, 1, 2, 2, 3]
    k = 2
    # input = [1]
    # k = 1
    print(s.topKFrequent(input, k))
