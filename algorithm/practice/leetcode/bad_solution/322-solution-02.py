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
        self.result = -1

    def get_all_group(self, total: int, coins: List[int], amount: int, count: int) -> int:
        """
        暴力穷举所有组合
        """
        # 退出条件
        if total >= amount:
            if total == amount:
                if count < self.result or self.result == -1:
                    self.result = count
                # print(f'\033[0;32m匹配到了{amount}:\033[0m', count)
            else:
                return
                # print(f'没有匹配到{amount}:', track)
            return total

        # 前序遍历
        for each_coin in coins:
            # ============= 核心算法 =============
            next_step_total = total + each_coin
            next_step_count = count+1
            # ===================================
            self.get_all_group(next_step_total, coins, amount, next_step_count)
            # 后序遍历

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :track 追踪 
        """
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        self.get_all_group(0, sorted(coins, reverse=True), amount, 0)

        return self.result


result = Solution().coinChange([5,2,1], 100)
print(result)
