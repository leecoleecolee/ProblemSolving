class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 처음엔 아래처럼 구현하는 걸 고려했는데, "cbacdcbc"의 결과값이 "acdb"인 것을 생각하면 이렇게 풀 순 없을 것 같다.
        # table = [0 for i in range(255)]
        # ret = ""

        # for char in s:
        #     if table[ord(char)] == 0:
        #         table[ord(char)] = 1
        #         ret += char
        # return ''.join(sorted(ret))

        # 왜 그럴까? 이 문제에서 말하는 '사전식 순서'란 글자 그대로 사전에서 가장 먼저 찾을 수 있는 순서를 말한다.
        # 그런데 인풋이 "cbacdcbc"로 들어올 경우엔 왜 "abcd"가 되지 않고 "acdb"가 되냐고? c와 b는 중복문자라서 삭제가 가능한데, d는 중복문자가 아니여서 삭제가 불가하기 때문이다.(위치 고정)
        # 결국 무턱대고 중복을 제거하면 안된다.


if __name__ == "__main__":
    s = Solution()
    input = "azzbcdefasdlkjlaaaa"
    print(s.removeDuplicateLetters(input))

    input = "bcabc"
    print(s.removeDuplicateLetters(input))

    input = "cbacdcbc"
    print(s.removeDuplicateLetters(input))
