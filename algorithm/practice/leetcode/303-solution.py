"""
303. 区域和检索 - 数组不可变
https://leetcode-cn.com/problems/range-sum-query-immutable/

给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

题目描述:
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

sample:
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1

我的解题思路:
如果是小白的话, 马上想到的方法是从 left 到 right 去数组, 这样的时间复杂度是 O(N). 
但是我们有一种更加高效的办法, 可以使得时间复杂度降到 O(1)，这就是前缀和.
所谓前缀和，就是一个数组, 它记录着「另外一个数组」的和值。
这个数组的某个下标对应位置，存放着「另外一个数组」的对应下标之前所有值的和。用数学表达类似这样：
y0 = x0
y1 = x0 + x1
y2 = x0 + x1+ x2

"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_list = [0]  # 给个初始的 0
        for i in range(len(nums)):
            # prefix_sum 数组，第 i 个位置的元素是: 原始数组[i] + prefix_sum_list[i-1]
            # prefix_sum[x] 为 nums[x-1] 之前所有数字之和
            self.prefix_sum_list.append(
                nums[i] + self.prefix_sum_list[i]
            )


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum_list[right + 1] - self.prefix_sum_list[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3,4,5])
obj.sumRange(0, 2)
# param_1 = obj.sumRange(left,right)