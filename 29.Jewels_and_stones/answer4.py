class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


if __name__ == "__main__":
    s = Solution()
    input1 = "aA"
    input2 = "aAAbbbb"
    print(s.numJewelsInStones(input1, input2))
