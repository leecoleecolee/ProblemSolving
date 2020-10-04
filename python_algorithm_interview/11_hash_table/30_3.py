class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_i = {}
        start_i = 0
        ret = 0
        for i, char in enumerate(s):
            if char in used_i and start_i <= used_i[char]:
                start_i = used_i[char] + 1
            else:
                ret = max(ret, i - start_i + 1)
            used_i[char] = i
        return ret

sol = Solution()
s = "abcabcbb"
print (sol.lengthOfLongestSubstring(s))
