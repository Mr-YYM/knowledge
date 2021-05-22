import time

class Solution:
    """
    动态规划法。
    """
    result_dict = {}  # 动态规划，以空间换时间
    def fib(self, n: int) -> int:
        if n in self.result_dict:
            return self.result_dict[n]
        if n<=1:  # 一开始忘记考虑 0 的情况（n == 1 or n == 2），结果递归过深，爆了
            return n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            self.result_dict[n] = result
            return result


print(Solution().fib(0))
