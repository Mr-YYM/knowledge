"""
560. 和为 K 的子数组
https://leetcode-cn.com/problems/subarray-sum-equals-k/

题目描述:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

我的解题思路:
1. 前缀和
2. 使用字典（哈希表）缓存次数
3. 取巧（字典的 key 为前缀和，vaule 为次数）

遇到的问题:
1. 暴力解法无法通过
2. 利用字典缓存的理解不够
3. => 下方代码解析 <=

执行用时： 64 ms , 在所有 Python3 提交中击败了 92.46% 的用户 内存消耗： 17.2 MB , 
在所有 Python3 提交中击败了 32.08% 的用户 
通过测试用例： 89 / 89
"""
from typing import List
from pprint import pprint


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        # 哈希表缓存，搜索时间为 O(1)
        # key 作为前缀和集合
        # vaule 计数, 记录每个元素的个数
        prefix_sum_dict = {0:1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num

            # ============= 下方代码解析 =============
            # 「次数计算」 与 「前缀和计数」他们的顺序不能调换
            # 如果遇到 k = 0 这种情况, 会导致出错
            # ======================================

            # =============== 次数计算 ===============
            target_nums = prefix_sum - k
            # 如果字典里有目标结果，有多少个就加上多少个。
            if target_nums in prefix_sum_dict:
                count += prefix_sum_dict[target_nums]

            # =============== 前缀和计数 ===============
            if prefix_sum not in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] = 1
            else:
                prefix_sum_dict[prefix_sum] += 1

        # pprint(prefix_sum_dict)
        return count


result = Solution().subarraySum([1,-1],0)
print(result)