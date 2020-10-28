class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # --- 실용적 해결: set을 이용한 방법 (28ms / 14.3MB)
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set1 & set2)

        # --- 알고리즘: 파이썬 검색(in) 활용 (76ms / 14.3MB)
        # ret = []
        # for num in nums1:
        #     if num in nums2 and not num in ret: # 이 부분을 이진 검색으로 바꾸는 풀이가 가능한가? 파이썬의 검색은 그럼 뭐지? 이진 검색이 아닌가?
        #         ret.append(num)
        # return ret

        # --- 알고리즘: 파이썬 검색(in)과 set 자료형 활용 (68ms / 14.3MB)
        # ret = set() # 리스트 대신 set로.
        # for num in nums1:
        #     if num in nums2: # 탐색을 사용자가 따로 할 필요 없이, 자료형에서 알아서 중복을 피해줌. 
        #         ret.add(num) # set에서는 append 대신 add로.
        # return ret

        # --- 알고리즘: 이진 검색 (44ms / 14.3MB)
        ret = set()
        if not nums2:
            return ret
        nums2.sort()
        for num in nums1:
            i2 = bisect.bisect_left(nums2, num)
            if len(nums2) > i2 and num == nums2[i2]:
                ret.add(num)
        return ret

'''
* bisect
    * https://docs.python.org/ko/3/library/bisect.html
    * https://folivora.tistory.com/83
'''