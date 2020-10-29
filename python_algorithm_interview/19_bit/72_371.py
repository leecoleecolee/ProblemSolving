class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a > int_max:
            a = ~(a ^ mask)
        return a