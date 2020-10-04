import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count


if __name__ == "__main__":
    s = Solution()
    input1 = "aA"
    input2 = "aAAbbbb"
    print(s.numJewelsInStones(input1, input2))
