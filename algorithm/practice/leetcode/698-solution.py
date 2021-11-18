"""
698. 划分为k个相等的子集
https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/

题目描述:
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。


"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 排除特殊情况
        if k > len(nums):
            return False
        
        if sum(nums) % k != 0:
            return False
        
        # k 个 🪣 ，记录每个 🪣 的数字之和
        buckets = [0] * k
        target = sum(nums) / k

        # sorted(nums, reverse=True) 排个序，运行更快
        return self.backtrack(sorted(nums, reverse=True), 0, buckets, target)

    def backtrack(self, nums: List[int], index: int, buckets: List[int], target: int):

        # 穷举完成，检查
        if index == len(nums):
            # 检查每个 bucket
            for each_bucket in buckets:
                if each_bucket != target:
                    return False
            return True
        
        # 穷举 nums[index] 可能装入的桶
        for i, each_bucket in enumerate(buckets):
            # 剪枝
            if each_bucket + nums[index] > target:
                continue
            
            # 装 🪣
            buckets[i] += nums[index]

            if self.backtrack(nums, index+1, buckets, target):
                return True
            
            # 撤销选择
            buckets[i] -= nums[index]
        
        return False
