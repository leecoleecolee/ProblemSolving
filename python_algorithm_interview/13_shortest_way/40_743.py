from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        # --- 깊이 우선 탐색
        '''
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))

        # dist = {node: float('inf') for node in range(1, N+1)}
        dist = {}
        for i in range(1, N+1):
            dist[i] = float('inf')
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())

        if ans < float('inf'):
            return ans
        else:
            return -1
        '''

        # --- 다익스트라 알고리즘
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w)) # graph: { 현재 노드: (다음 노드, 시간) }
        
        Q = [(0,K)] # Q: [ (총 시간, 도착 노드) ]
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time # dist: { 도착 노드: 최소 총 시간 }
                for v,w in graph[node]:
                    heapq.heappush(Q, (time+w, v))

        if len(dist) != N:
            return -1
        return max(dist.values())