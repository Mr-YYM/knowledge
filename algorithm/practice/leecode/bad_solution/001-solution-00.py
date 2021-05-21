from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力解法
        """
        nums_length = len(nums)
        for i in range(nums_length - 1):
            for j in range(i+1, nums_length):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([3,3], 6))