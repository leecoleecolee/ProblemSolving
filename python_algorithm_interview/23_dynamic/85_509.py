# --- 재귀 브루트포스 / 1000ms --- #
# class Solution:
#     dict = collections.defaultdict(int)
#     def fib(self, N: int) -> int:
#         if N == 0:
#             return 0
#         elif N == 1:
#             return 1
#         return self.fib(N - 1) + self.fib(N - 2)

# --- 하향 메모이제이션 / 32ms --- #
# class Solution:
#     dict = collections.defaultdict(int)
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         if self.dict[N]:
#             return self.dict[N]
#         self.dict[N] = self.fib(N - 1) + self.fib(N - 2)
#         return self.dict[N]

# --- 상향 타뷸레이션 / 28ms --- #
class Solution:
    dict = collections.defaultdict(int)
    def fib(self, N: int) -> int:
        self.dict[1] = 1
        for i in range(2, N + 1):
            self.dict[i] = self.dict[i - 1] + self.dict[i - 2]
        return self.dict[N]