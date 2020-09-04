from typing import *


# 파이쏘닉한 방식. 짝수번째 값이 가장 작은 값이므로, 2칸씩 건너뛴 값들의 합을 리턴한다.
# 슬라이싱을 사용한 덕분에 성능이 가장 좋다.
class Solution:
    def answer3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
