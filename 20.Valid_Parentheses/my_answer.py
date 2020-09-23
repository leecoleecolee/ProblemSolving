class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["dummy"]

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and stack.pop() != '(':
                return False
            elif s[i] == ']' and stack.pop() != '[':
                return False
            elif s[i] == '}' and stack.pop() != '{':
                return False
        return stack.pop() == "dummy"


if __name__ == "__main__":
    s = Solution()
    input = "()[]{}"
    print(s.isValid(input))

    input = "()[]{"
    print(s.isValid(input))

    input = "a()sdjklf"
    print(s.isValid(input))

    input = ""
    print(s.isValid(input))

    input = "["
    print(s.isValid(input))

    input = "]"
    print(s.isValid(input))
