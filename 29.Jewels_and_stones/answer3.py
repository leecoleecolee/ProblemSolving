import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)
        count = 0
        # 만약 Counter에 존재하지 않는 키의 경우 KeyError를 발생시키는게 아니라 0을 출력해주므로 예외처리가 필요없다.
        for char in J:
            count += freqs[char]

        return count


if __name__ == "__main__":
    s = Solution()
    input1 = "aA"
    input2 = "aAAbbbb"
    print(s.numJewelsInStones(input1, input2))
