class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # abcabcbb
    # 보통같으면 시작점, 끝에 대한 변수를 이용
    # 하지만 이 문제는 시작점에 대한 변수만 있으면 된다.
    # 중복검사를 할 때 해쉬테이블을 사용한다. 파이썬에서는 dict이 해쉬테이블이므로 그냥 사용하면됨.
    # 이 문제의 return 값은 int형. 문자열의 길이다. 문자열 자체가 아니다!.
    # start -> left pointer
        used = {}
        max_length = start = 0 

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index
        return max_length
