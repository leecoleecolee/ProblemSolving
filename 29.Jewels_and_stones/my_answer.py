class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        if not J or not S:
            return -1

        count = 0
        for char in S:
            if char in J:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    input1 = "aA"
    input2 = "aAAbbbb"
    print(s.numJewelsInStones(input1, input2))
