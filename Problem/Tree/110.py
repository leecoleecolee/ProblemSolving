class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node: TreeNode, height: int) -> int:
            if not node:
                return height
            left = getHeight(node.left, height + 1)
            right = getHeight(node.right, height + 1)
            diff = abs(right - left)
            if diff > 1:
                return -1
            return max(left, right)
        ret = getHeight(root, 0)
        if ret == -1:
            return False
        return True
