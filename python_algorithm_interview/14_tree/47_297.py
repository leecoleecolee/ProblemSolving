import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        # --- BFS
        # queue = collections.deque([root])
        # array = ["#"]

        # while queue:
        #     node = queue.popleft()
        #     if node:
        #         queue.append(node.left)
        #         queue.append(node.right)
        #         array.append(str(node.val))
        #     else:
        #         array.append("#")
            
        # return ' '.join(array)

        # --- 재귀
        vals = ["#"]

        def rec(node):
            if node:
                vals.append(str(node.val))
                rec(node.left)
                rec(node.right)
            else:
                vals.append("#")

        rec(root)
        return ' '.join(vals)

    def deserialize(self, data):
        # --- BFS
        # nodes = data.split()

        # if nodes[1] == "#":
        #     return None

        # root = TreeNode(int(nodes[1]))
        # queue = collections.deque([root])
        
        # index = 2

        # while queue:
        #     node = queue.popleft()

        #     if nodes[index] is not "#":
        #         node.left = TreeNode(int(nodes[index]))
        #         queue.append(node.left)
        #     index += 1

        #     if nodes[index] is not "#":
        #         node.right = TreeNode(int(nodes[index]))
        #         queue.append(node.right)
        #     index += 1

        # return root

        # --- 재귀
        vals = collections.deque(data.split())
        # vals = iter(data.split())
        
        vals.popleft()
        # next(vals)

        def rec():
            val = vals.popleft()
            # val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = rec()
            node.right = rec()
            return node
        
        return rec()
