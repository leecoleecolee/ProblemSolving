class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        ret = []
        for l in count.most_common(k):
            ret.append(l[0])
        return ret
