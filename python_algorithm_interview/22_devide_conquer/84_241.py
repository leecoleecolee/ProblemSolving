class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def get_all(left, right, v):
            ret = []
            for l in left:
                for r in right:
                    ret.append(eval(str(l) + v + str(r))) # eval(): 문자열을 숫자(정수나 실수)로 변환하는 함수. 연산자가 있으면 계산까지 해준다.
            return ret

        if input.isdigit():
            return [int(input)]
        
        ret = []
        for i, v in enumerate(input):
            if v in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                ret.extend(get_all(left, right, v)) # .extend(): append와 다르게 리스트를 요소로 분리해서 추가해줌.
        
        return ret