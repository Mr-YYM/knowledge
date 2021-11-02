"""
560. 和为 K 的子数组
https://leetcode-cn.com/problems/subarray-sum-equals-k/

题目描述:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # 得到前缀和列表
        prefix_sum_list = [0]
        for i in range(len(nums)):
            prefix_sum_list.append(
                prefix_sum_list[i] + nums[i]
            )
        
        print(prefix_sum_list)
        
        # 找出所有结果
        count = 0
        nums_length = len(prefix_sum_list)
        print(f'nums_length: {nums_length}')
        for left in range(nums_length):
            for right in range(left + 1, nums_length):
                if prefix_sum_list[right] - prefix_sum_list[left] == k:
                    # print(f'{prefix_sum_list[right]} - {prefix_sum_list[left]}')
                    count += 1
        
        return count

result = Solution().subarraySum([1,2,3],3)
print(result)