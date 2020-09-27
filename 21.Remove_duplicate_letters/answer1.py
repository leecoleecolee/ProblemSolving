import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 정렬된 중복없는 리스트를 만들어서, 원본 문자열에서 중복있는 것은 최대한 앞에 남기면서 삭제하고, 중복 없는 것은 그 자리에 남긴다.
        # sorted 안하면 bcabc의 결과값이 bca이다. sorted라는 정렬함수는 시퀀스 자료형 뿐만 아니라 순서에 구애받지 않는 자료형에도 적용할 수 있습니다. 정렬된 결과는 list로 반환됩니다.
        for char in sorted(set(s)):
            suffix = s[s.index(char):]  # s는 여전히 문자열이다. 슬라이싱해준다.
            if set(s) == set(suffix):
                # 제일앞에 char를 남기고, suffix에서 중복문자를 제거한다.
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


if __name__ == "__main__":
    s = Solution()
    # input = "azzbcdefasdlkjlaaaa"
    # print(s.removeDuplicateLetters(input))

    # input = "bcabc"
    # print(s.removeDuplicateLetters(input))

    input = "cbacdcbc"
    print(s.removeDuplicateLetters(input))
