class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 이 문제는 값의 중복이 가능하다.
            # 따라서 조합의 풀이를 이용하자.
        # 입력으로 들어온 candidates의 값은 변경하지 않는다.
            # 인덱스를 이용해서 조작하자.
        ret = []
        if not candidates:
            return ret
        def dfs(csum: int, index: int, path: List[int]):
            # 재귀의 종료 조건
                # csum == 0 or csum < 0
            if csum == 0:
                ret.append(path)
                return
            elif csum < 0:
                return
            else:
                # 반목문의 시작 지점이 자기 자신의 인덱스. 따라서 자신을 포함해서 계속 쭉 dfs 할 수 있게 된다.
                for i in range(index, len(candidates)):
                    dfs(csum - candidates[i], i, path + [candidates[i]])
        
        # dfs 시작
        dfs(target, 0, [])
        return ret
