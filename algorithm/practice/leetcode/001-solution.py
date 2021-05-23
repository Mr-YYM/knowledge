from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        相较于暴力解法，使用空间换时间的思想进行解题
        假设我们 x + y = target, x 通过遍历得到，y 就是 target - x
        我们定义一个字典（对应哈希表数据结构）, 在遍历的过程中顺便记录每个值对应的 index 位置 {value: index}
        这样 y 值我们不再 for 一层来查找，而是通过在字典中查找，由于「哈希表」的搜索时间复杂度只有 O(1) 一次能够大幅提高效率
        """
        y_index_dict = {}
        for x_index, x in enumerate(nums):
            y = target - x
            if y not in y_index_dict:
                y_index_dict[x] = x_index
                continue
            y_index = y_index_dict[y]
            return [x_index, y_index]

print(Solution().twoSum([3,3], 6))
