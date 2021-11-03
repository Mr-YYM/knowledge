"""
1094. 拼车
https://leetcode-cn.com/problems/car-pooling/

问题描述:
假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：

必须接送的乘客数量；
乘客的上车地点；
以及乘客的下车地点。
这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所有乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。

提示：
你可以假设乘客会自觉遵守 “先下后上” 的良好素质
trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000

我的解题思路:


遇到的问题:


"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 使用一个数组，记录汽车到达每一站的时候，当前的乘客数量
        # 为了提高效率，我们使用差分数组
        # 其实就是记录每个站点上下车人数，上车 + 下车 -
        passager_count_diff_list = [0] * 1000

        for each_trip in trips:
            boarding_passager_nums, boarding_station, get_off_station = each_trip

            passager_count_diff_list[boarding_station] += boarding_passager_nums
            passager_count_diff_list[get_off_station] -= boarding_passager_nums

        station_count = 0  # 乘客数
        for each_count_diff in passager_count_diff_list:
            station_count += each_count_diff
            print(station_count, end=' ')
            if station_count > capacity:
                return False
        
        return True



result = Solution().carPooling([[2,1,5],[3,3,7]],4)
print(result)
