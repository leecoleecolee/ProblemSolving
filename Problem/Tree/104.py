# bfs -> 재귀x , queue
        if not root:
            return 0
        depth = 0
        queue = collections.deque([root]) # deqeue -> iterable
        while queue:
            depth += 1
            for _ in range(len(queue)): # 눈여겨서
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
