import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # --- 리스트: 시간복잡도 O(n^2) / 공간복잡도 O(n)
        # ret = []
        # for num in nums:
        #     if num not in ret:
        #         ret.append(num)
        #     else:
        #         ret.remove(num)
        # return ret.pop()

        # --- 해시 테이블: 시간복잡도 O(n) / 공간복잡도 O(n)
        # hash = collections.defaultdict(int)
        # for num in nums:
        #     hash[num] += 1
        # for key in hash:
        #     if hash[key] == 1:
        #         return key

        # --- xor 풀이: 시간복잡도 O(n) / 공간복잡도 O(1)
        result = 0
        for num in nums:
            result ^= num
        return result
