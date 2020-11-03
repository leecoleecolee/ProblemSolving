import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # --- 브루트포스: 시간초과
        # ret = []
        # for i in range(len(nums) - (k - 1)):
        #     ret.append(max(nums[i:i + k]))
        # return ret

        # --- 큐를 이용한 최적화: 이것도 시간초과네?
        # ret = []
        # window_queue = collections.deque() # 안넣으면 기본적으로 리스튼가?
        # max_value = float("-inf")

        # for i, v in enumerate(nums):
        #     window_queue.append(v)
        #     if i < k - 1:
        #         continue

        #     if max_value == float("-inf"):
        #         max_value = max(window_queue)
        #     elif v > max_value:
        #         max_value = v
            
        #     ret.append(max_value)

        #     if window_queue.popleft() == max_value:
        #         max_value = float("-inf")
        
        # return ret

        # --- 큐를 이용한 최적화2
        ret = []
        deque = collections.deque()
        for i, v in enumerate(nums):
            while deque and v >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            if deque[0] == i - k:
                deque.popleft()
            ret.append(nums[deque[0]])
        return ret[k - 1:]
