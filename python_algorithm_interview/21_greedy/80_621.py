import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ret = 0
        count = collections.Counter(tasks)
        while True:
            most_len = 0
            for task, _ in count.most_common(n + 1): # most_common 메서드는 최대 힙과 같은 기능.
                ret += 1
                most_len += 1
                count.subtract(task) # value값을 1씩 감소
                count += collections.Counter() # 0 이하인 값을 제거하는 테크닉
            if not count:
                break
            ret += n + 1 - most_len

        return ret