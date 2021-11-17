"""
46. 全排列
https://leetcode-cn.com/problems/permutations/

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrace(nums, track)
        return self.res

    def backtrace(self, nums: List[int], track: List[int]):
        # 结束条件
        if len(track) == len(nums):
            self.res.append(list(track))  # list(track) 记得要这样哦，创建一个新的 list，不然会有神奇的引用重复问题
            return
        
        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.backtrace(nums, track)
            track.pop()


result = Solution().permute([1,2,3])
print(result)
