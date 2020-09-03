class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' pretreatment'''
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        if (len(strs) % 2 == 0):
            idx1 = len(strs) // 2 - 1
            idx2 = idx1 + 1
        else:
            idx1 = len(strs) // 2 - 1
            idx2 = idx1 + 2
        while (idx1 > -1):
            if (strs[idx1] != strs[idx2]):
                return (False)
            idx1 -= 1
            idx2 += 1
        return (True)


if __name__ == "__main__":
    a = Solution()
    s = "ab"
    print(a.isPalindrome(s))
