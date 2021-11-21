"""
322. 零钱兑换
https://leetcode-cn.com/problems/coin-change/

题目描述:
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.result_dict = {}

    def dp(self, coins: List[int], amount: int):
        """
        动态规划解法
        """
        # 退出条件
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.result_dict:
            return self.result_dict[amount]

        result = float('inf')  # float('inf') 是一个很大的数
        for each_coin in coins:
            sub_problem = self.dp(coins, amount - each_coin)
            if sub_problem == -1:
                continue
            result = min(result, sub_problem + 1)
        
        if result == float('inf'):
            self.result_dict[amount] = -1
        else:
            self.result_dict[amount] = result
        return self.result_dict[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :track 追踪 
        """
        return self.dp(coins, amount)


result = Solution().coinChange([1,2,5], 100)
print(result)
