class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        count = 0
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count


if __name__ == "__main__":
    s = Solution()
    input1 = "aA"
    input2 = "aAAbbbb"
    print(s.numJewelsInStones(input1, input2))
