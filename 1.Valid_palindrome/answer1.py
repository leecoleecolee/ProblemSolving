class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pretreatment
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        # check palindrome
        while (len(strs) > 1):
            if strs.pop(0) != strs.pop():
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    #s = "ab"
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))
