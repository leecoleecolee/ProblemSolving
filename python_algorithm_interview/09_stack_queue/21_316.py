'''
* 문제
중복된 문자를 제외하고 사전으로 제일 앞서도록 나열하라.
in) "cbacdcbc"
out) "acdb" # "abcd"가 아님!

* [x] 1회차
재귀 풀이 - 역시 리턴 부분에서 버벅임. 그래도 이 문제는 어렵지 않은 재귀여서 이해가 수월했다.
스택 풀이 - 아직 스택에도 익숙하지 않고, 카운터 등을 사용하는 것을 떠올리기 쉽지 않음.
'''

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # --- 재귀
        # set_s = set(s)
        # for char in sorted(set_s):
        #     subset = s[s.index(char):]
        #     if set_s == set(subset):
        #         return char + self.removeDuplicateLetters(subset.replace(char, ""))
        # return ""

        # --- 스택
        counter = collections.Counter(s)
        stack = []

        for char in s:
            counter[char] -= 1
            if char in stack: # 정확히는 스택의 기능이 아니므로, 스택으로 풀려면 따로 seen을 만들어주는 것임.
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)