class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # --- 문자열에서 1을 세는 방법
        # return bin(x ^ y).count('1')

        # --- 비트계산
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1) # 이게 뭐지?
        return y