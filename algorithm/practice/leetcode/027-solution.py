"""
https://leetcode-cn.com/problems/remove-element/
https://app6aigdwnl3832.h5.xiaoeknow.com/v1/course/text/i_614d8d4ae4b04518c61771e3?type=2&pro_id=p_6142fa72e4b0dfaf7fa47f69&from_multi_course=1&is_redirect=1


题目描述:
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

我的解题思路:
1. 跟第 26 题相同的思想, 使用双指针。
2. 「探寻指针」不断往前寻找不一样的元素

过程中遇到的问题:
1. 返回的时候，以为跟第 26 题一样，返回 operating_pointer + 1，其实并不需要这样。
   因为 27 题是修改后才往前移动的，而 26 题是移动后再修改。

   为什么有这种差异:
   因为 26 题是验证重复，第一个元素必然不重复，所以不存在第一个元素被修改的可能性。
   27 题是比较一个外部传入数据，所以存在第一个被修改的可能性。

通过 28 ms	14.9 MB	Python3	2021/11/01 23:46

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 定义两个指针
        operating_pointer = 0  # 操作指针，负责修改数组元素 nums[operating_pointer] = nums[seeking_pointer]
        seeking_pointer = 0  # 探寻指针，走在前面，找到与 val 不一样的元素

        for _ in nums:
            # 遇到不同元素就修改「操作指针」对应的值，并推进「操作指针」
            if nums[seeking_pointer] != val:
                nums[operating_pointer] = nums[seeking_pointer]
                operating_pointer += 1
            
            seeking_pointer += 1
        return operating_pointer


result = Solution().removeElement([3,2,2,3], 3)
print(result)