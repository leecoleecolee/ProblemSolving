import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # --- 해시 테이블(defaultdict)을 이용한 풀이
        '''
        table = collections.defaultdict(int)
        ret = 0
        for s in S:
            table[s] += 1
        for j in J:
            ret += table[j]
        return ret
        '''

        # --- 해시 테이블(Counter)을 이용한 풀이
        table = collections.Counter(S)
        ret = 0
        for j in J:
            ret += table[j]
        return ret

        # --- 파이썬다운 방식(리스트 컴프리헨션)
        '''
        return sum(s in J for s in S)
        '''

# ---
sol = Solution()
J = "aA"
S = "aAAbbbb"
print (sol.numJewelsInStones(J, S))
