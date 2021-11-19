"""
509. 斐波那契数
https://leetcode-cn.com/problems/fibonacci-number/

题目描述:
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

"""

import time


def count_time(func):
    """
    计时装饰器，用在递归上，只打印全部时间
    还没完全搞懂！！！
    """
    count_time.level = 0

    def wrap(*args, **kwargs):

        if count_time.level == 0:
            count_time.level += 1
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'{func.__name__} which consume time is :', end_time - start_time)
        else:
            result = func(*args, **kwargs)

        count_time.level -= 1

        return result

    return wrap


class Solution:
    """
    动态规划法。
    """
    result_dict = {}  # 动态规划，以空间换时间

    @count_time
    def fib(self, n: int) -> int:
        if n in self.result_dict:
            return self.result_dict[n]
        if n <= 1:  # 一开始忘记考虑 0 的情况（n == 1 or n == 2），结果递归过深，爆了
            return n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            self.result_dict[n] = result
            return result


print(Solution().fib(33))
