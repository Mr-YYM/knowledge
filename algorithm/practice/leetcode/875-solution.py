"""
875. 爱吃香蕉的珂珂
https://leetcode-cn.com/problems/koko-eating-bananas/

问题描述:
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

sample:
输入: piles = [3,6,7,11], H = 8
输出: 4

输入: piles = [30,11,23,4,20], H = 5
输出: 30

我的解题思路:


过程遇到的问题:


"""

from typing import List


class Solution:

    def get_eating_hours(self, piles: List[int], k: int) -> int:
        hours = 0
        for each_pile in piles:
            hours += int(each_pile / k)
            if each_pile % k > 0:
                hours += 1
        
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_range_eating_speed = 1
        max_range_eating_speed = 10**9

        while min_range_eating_speed <= max_range_eating_speed:
            mid_eating_speed = min_range_eating_speed + (max_range_eating_speed - min_range_eating_speed) / 2
            mid_eating_speed = int(mid_eating_speed)
            eating_hours = self.get_eating_hours(piles, mid_eating_speed)

            if eating_hours <= h:
                max_range_eating_speed = mid_eating_speed - 1
            else:
                min_range_eating_speed = mid_eating_speed + 1
            
            print(min_range_eating_speed, max_range_eating_speed, mid_eating_speed)
        
        return min_range_eating_speed

result = Solution().minEatingSpeed([30,11,23,4,20], 6)
print(result)
