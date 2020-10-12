class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 1. 인접행렬 만들기
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 2. 우선순위 큐 만들ㄹ기
        Q = [(0, K)]
        
        # 현재 노드부터의 거리를 담을 dist 딕셔너리
        dist = collections.defaultdict(int)
        
        # 4. 반복 시작
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                # 5. 시간 갱신
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == N:
            return max(dist.values())
        return -1
            
