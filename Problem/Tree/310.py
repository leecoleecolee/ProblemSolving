class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:        
        if n <= 1:
            return [0]
        # 1. 인접행렬
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # 2. 첫 번째 가지를 찾는다.
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2: # 1개또는 2개가 남는다면 종료된다.
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
