'''
* 문제
괄호가 유효한지 판별하라.
in) ()[]{}
out) true

* [x] 1회차
안에 괄호 말고 다른 문자가 들어올 때도 동작하게끔 풀어보았다.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in dict:
                stack.append(char)
            elif char in dict.values():
                if not stack or dict[stack[-1]] != char:
                    return False
                stack.pop()

        if stack:
            return False
        
        return True

# ---
sol = Solution()
s = "(abc)[f{de]}"
s = "(abc)[f{de}]"
print (sol.isValid(s))
