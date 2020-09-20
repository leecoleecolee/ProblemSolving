from typing import List
import collections

# ---
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left = []
#         right = []
#         for num in nums:
#         # for i, num in enumerate(nums):
#             # if i == len(nums) - 1:
#                 # break
#             if not left:
#                 left.append(num)
#             else:
#                 left.append(left[-1] * num)
#         for num in nums[::-1]:
#             if not right:
#                 right.append(num)
#             else:
#                 right.append(right[-1] * num)
#         right = right[::-1]
#         # print (left)
#         # print (right)

#         ret = []
#         for i in range(len(nums)):
#             if i - 1 >= 0 and i + 1 < len(nums):
#                 ret.append(left[i - 1] * right[i + 1])
#             elif i - 1 < 0 and i + 1 < len(nums):
#                 ret.append(right[i + 1])
#             elif i - 1 >= 0 and i + 1 >= len(nums):
#                 ret.append(left[i - 1])
#             else:
#                 ret.append(1)
#         return ret

# ---
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, backward = collections.deque(), collections.deque()
        f, b = 1, 1
        
        for i, num in enumerate(nums):
            forward.append(f)
            f *= num
            backward.appendleft(b) # deque를 이용한 appendleft
            b *= nums[len(nums) - 1 - i]

        # print (forward)
        # print (backward)
        # print (list(zip(forward, backward))) # zip()

        return [a * b for a, b in zip(forward, backward)] # 리스트 컴프리헨션과 zip()을 이용한 두 리스트의 곱연산

# ---
sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))