class Solution:
    def searchMatrix(self, matrix, target):
        # --- 내 방법 (28ms / 18.8MB)
        for m in matrix:
            if not m or m[0] > target:
                break
            i = bisect.bisect_left(m, target)
            if i < len(m) and m[i] == target:
                return True
        return False
            