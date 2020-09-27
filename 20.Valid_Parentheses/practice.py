class Solution:
    def isValid(self, s: str) -> bool:
        # stack = ['dummy']

        # for char in s:
        #     if char == '(' or char == '[' or char == '{':
        #         stack.append(char)
        #     elif char == ')' and stack.pop() != '(':
        #         return False
        #     elif char == ']' and stack.pop() != '[':
        #         return False
        #     elif char == '}' and stack.pop() != '{':
        #         return False
        # return stack.pop() == "dummy"

        # stack = []
        # table = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '[',
        # }

        # for char in s:
        #     if char not in table:
        #         stack.append(char)
        #     elif not stack or table[char] != stack.pop():
        #         return False
        # return not stack


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
