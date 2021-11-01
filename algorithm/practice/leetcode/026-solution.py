"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
https://app6aigdwnl3832.h5.xiaoeknow.com/v1/course/text/i_614d8d4ae4b04518c61771e3?type=2&pro_id=p_6142fa72e4b0dfaf7fa47f69&from_multi_course=1&is_redirect=1

题目描述:
给你一个有序数组 nums ，请你「原地」删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

我的解题思路:
1. 有序的数组, 保证了相同的元素是彼此挨着的。
2. 我们可以设计出两条指针，一条指针（探寻指针）负责往前推进，一路去寻找不一样的元素。
   另外一条就负责修改数组（操作指针），探寻指针每遇到一个不相同的元素，操作指针就向前一步并修改对应位置的值

过程中遇到的问题:
1. IndexError: list index out of range
一开始我把 `seeking_pointer += 1` 这一行放在循环开头，结果数组越界了。把它放到最后，问题解决。

结果:
执行结果：通过

执行用时：32 ms , 在所有 Python3 提交中击败了 91.59 % 的用户 
内存消耗： 15.6 MB , 在所有 Python3 提交中击败了 54.25% 的用户 
通过测试用例： 362 / 362

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 定义两个指针
        operating_pointer = 0  # 操作指针，负责修改数组元素用 nums[operating_pointer] = nums[seeking_pointer]
        seeking_pointer = 0  # 探寻指针，走在前面，找到不一样的元素
        for _ in nums:
            # 如果出现不一样的元素, 操作指针向前一步，然后修改「它指向的内容」为「探寻指针的值」
            if nums[seeking_pointer] != nums[operating_pointer]:
                operating_pointer += 1
                nums[operating_pointer] = nums[seeking_pointer]

            # 如果一样，探寻指针继续向前。开始下一轮循环
            seeking_pointer += 1  # 探寻指针往前走一步

        
        # 长度就是「操作指针」的 index + 1
        return operating_pointer + 1


result = Solution().removeDuplicates([0,0,1,2,2,3,3])
print(result)
