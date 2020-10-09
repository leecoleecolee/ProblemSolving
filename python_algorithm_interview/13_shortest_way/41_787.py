from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w)) # graph: { 현재 노드: (다음 노드, 가격) }

        Q = [(0, src, 0)] # Q: [ (가격, 노드, 통과한 경유지 수) ]

        while Q:
            now_price, now_node, k = heapq.heappop(Q)
            if now_node == dst:
                return now_price
            if k <= K:
                for next_node, next_price in graph[now_node]:
                    heapq.heappush(Q, (now_price + next_price, next_node, k + 1))

        '''
        Q: (0, 0, 0)X (100, 1, 1)X (500, 2, 1)O
        '''

        return -1