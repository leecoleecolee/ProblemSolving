class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 부분집합의 개수: 2^n
        # 종료 조건이 필요없다.
        # 이전 문제와 동일하게 이번 문제도 배열 자체는 그대로 사용하고 인덱스를 조절하자.
            # 아까전에는 자기 자신을 그대로 사용했지만 이번에는 반복이 진행되면
            # 바로 다음으로 넘어가기 때문에 + 1 을 해주자.
        ret = []
        length = len(nums)
        def dfs(index: int, path: List[int]):
            ret.append(path)
            for i in range(index, length):
                dfs(i + 1, path + [nums[i]])
        # dfs 시작
        dfs(0, [])
        return ret
