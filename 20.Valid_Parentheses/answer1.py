class Solution:
    def isValid(self, s: str) -> bool:
        # 참고로 이 풀이는 인풋으로 open brackets만 들어올 떄 적용할 수 있는 방법이다.
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return not stack


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
