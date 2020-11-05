# https://leetcode.com/problems/minimum-window-substring/

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # --- 투 포인터로 최적화 ---#
        t_count = collections.Counter(t)
        need_len = len(t)
        left = start = end = 0
        for right, v in enumerate(s, 1):
        # right는 1부터 시작. index에 +1 된다고 보면 됨.
            if t_count[v] > 0:
                need_len -= 1
            t_count[v] -= 1
            # Counter은 없는 키값에도 접근할 수 있으며, 심지어 값이 0일 때 뺄셈 연산을 해서 음수를 저장할 수도 있다.
            if need_len == 0:
                while t_count[s[left]] < 0:
                    t_count[s[left]] += 1
                    left += 1
                if not end or right - left < end - start:
                    start, end = left, right
                    t_count[s[left]] += 1
                    left += 1
                    need_len += 1
        return s[start:end]

        # # --- enumerate(s)로 할 시 right에 부분적으로 1을 더해줘야하는 불편함 --- #
        # t_count = collections.Counter(t)
        # need_len = len(t)
        # left = start = end = 0
        # for right, v in enumerate(s):
        #     if t_count[v] > 0:
        #         need_len -= 1
        #     t_count[v] -= 1
        #     if need_len == 0:
        #         while t_count[s[left]] < 0:
        #             t_count[s[left]] += 1
        #             left += 1
        #         if not end or right + 1 - left <= end - start:
        #             start, end = left, right + 1
        #             t_count[s[left]] += 1
        #             left += 1
        #             need_len += 1
        # return s[start:end]

        # #--- Counter로 좀 더 편한 풀이: 편하지만 시간이 오래 걸림. ---#
        # t_count = collections.Counter(t)
        # current_count = collections.Counter()
        # left = start = end = 0
        # for right, v in enumerate(s, 1):
        #     current_count[v] += 1
        #     while current_count & t_count == t_count:
        #         if not end or right - left < end - start:
        #             start, end = left, right
        #         current_count[s[left]] -= 1
        #         left += 1
        # return s[start:end]

'''
"ADABCOBAC"
"AABC"

"a"
"aa"
'''