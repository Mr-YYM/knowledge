"""
496. 下一个更大元素 I
https://leetcode-cn.com/problems/next-greater-element-i/

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]

解题思路:
单调队列

"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_dict = {}
        bigger_nums_stack = [] # 用一个栈记录比他大的数字
        # 从后往前遍历, 依序找出他们右边第一个比它大的数字
        for each_num in reversed(nums2):
            
            # 把 bigger_nums_stack 中比 each_num 小的数字去掉
            while bigger_nums_stack and bigger_nums_stack[-1] <= each_num:
                bigger_nums_stack.pop()

            # 去掉之后，取出最前面的那一个。然后把结果记录到一个字典里
            if bigger_nums_stack:
                result_dict[each_num] = bigger_nums_stack[-1]
            else:
                # 没有就是 -1
                result_dict[each_num] = -1

            bigger_nums_stack.append(each_num)  # 把数字压入栈


        return [result_dict[n] for n in nums1]


result = Solution().nextGreaterElement([4,1,2], [1,3,4,2])
print(result)
