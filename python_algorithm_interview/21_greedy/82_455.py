from typing import List
import heapq
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # # --- 우선순위 큐 --- #
        # g_heap = []
        # s_heap = []
        # for v in g:
        #     heapq.heappush(g_heap, -v)
        # for v in s:
        #     heapq.heappush(s_heap, -v)
        # ret = 0
        # while g_heap and s_heap:
        #     need = -heapq.heappop(g_heap)
        #     cookie = -heapq.heappop(s_heap)
        #     if need <= cookie:
        #         ret += 1
        #     else:
        #         heapq.heappush(s_heap, -cookie)
        # return ret

        # # --- 그리디 알고리즘 --- #
        # g.sort()
        # s.sort()
        # child = cookie = 0
        # while child < len(g) and cookie < len(s):
        #     if g[child] <= s[cookie]:
        #         child += 1
        #     cookie +=1
        # return child

        # --- 이진 검색 --- #
        g.sort()
        s.sort()
        ret = 0
        for cookie in s:
            child = bisect.bisect_right(g, cookie)
            if ret < child:
                ret += 1
        return ret