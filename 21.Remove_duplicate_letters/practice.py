import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 카운터에는 글자별로 남은 중복갯수를 저장, seen은 이미 만났던 문자를 저장할 것이고 이미 처리된 문자임을 뜻한다. stack은 반환할 문자열을 저장한다.
        # counter: a=1, b=2, c=4, d=1
        counter, seen, stack = collections.Counter(s), set(), []

        # counter: a=0, b=0, c=2, d=0
        # stack : a, c, d, b
        # seen  : b, a, c, d, b
        for char in s:
            # 문자를 검사하면서 중복갯수에서 삭제해준다.
            counter[char] -= 1
            # 만약 이미 처리된 문자라면 그냥 넘어간다.
            if char in seen:
                continue
            # 스택의 마지막 문자가 검사하는 문자보다 큰 아스키 값을 가지고 있으면서 '중복'이 남아있다면, 스택과 '처리된 문자 set'에서 삭제한다!
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            # 이번에 검사한 문자를 스택과 seen에 추가한다.
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

        counter = collections.Counter(s)
        seen = set()
        stack = []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    input = "azzbcdefasdlkjlaaaa"
    print(s.removeDuplicateLetters(input))

    input = "bcabc"
    print(s.removeDuplicateLetters(input))

    input = "cbacdcbc"
    print(s.removeDuplicateLetters(input))
