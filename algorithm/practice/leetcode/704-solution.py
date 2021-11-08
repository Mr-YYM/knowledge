"""
704. 二分查找
https://leetcode-cn.com/problems/binary-search/

问题描述:
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


我的解题思路:
1. 二分法

遇到的问题


"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            mid = int(mid)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


result = Solution().search([-1,0,3,5,9,12],1)
print(result)
