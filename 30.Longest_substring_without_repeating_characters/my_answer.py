import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = collections.defaultdict()
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                # 최대 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            used[char] = index

        return max_length


if __name__ == "__main__":
    s = Solution()
    input = "abcabcbb"
    # input = "bbbbbbbbb"
    # input = "pwwkew"
    print(s.lengthOfLongestSubstring(input))
