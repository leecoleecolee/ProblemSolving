class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # --- dfs 재귀 브루트포스
        # if not root:
        #     return 0
        # val = 0
        # if L <= root.val <= R:
        #     val = root.val
        # return val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        
        # --- dfs 재귀 가지치기
        # if not root:
        #     return 0
        # elif root.val < L:
        #     return self.rangeSumBST(root.right, L, R)
        # elif root.val > R:
        #     return self.rangeSumBST(root.left, L, R)
        # return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

        # --- dfs 반복
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum