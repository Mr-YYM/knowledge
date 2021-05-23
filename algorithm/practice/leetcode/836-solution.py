class Solution:
    """
    836. 矩形重叠[https://leetcode-cn.com/problems/rectangle-overlap/]
    解题思路: 投影法
    """
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 在判断重叠之前，要判断 rec 是否是一个矩形
        # 根据问题描述可知，(x2, y2) 是右上角的坐标
        # 所以一个矩形满足一下条件: 
        # x2 >= x1 && y2 >= y1
        if not (rec1[2] > rec1[0] and rec1[3] > rec1[1]):
            return False
        if not (rec2[2] > rec2[0] and rec2[3] > rec2[1]):
            return False
        # 根据投影法的思路，判断 x、y 轴上的投影是否存在重叠
        # 由于非重叠的情况较少，因此使用逆向的思路
        # 排除非重叠的情况，剩下的就是重叠了
        # 简单画图可知，两个矩形（x1,y1,x2,y2）(x3,y3,x4,y4) 不重叠
        # x 轴上就是以下两种情形
        # 右边不重叠：x3 >= x2 或者左边不重叠：x4 <= x1
        x_overlap = not (rec2[0] >= rec1[2] or rec2[2] <= rec1[0])
        # y 轴上就是以下两种情形
        # 上边不重叠：y3 >= y2 或者下边不重叠：y4 <= y1
        y_overlap = not (rec2[1] >= rec1[3] or rec2[3] <= rec1[1])

        # 简单画图可知，只有 x y 轴同时存在重叠，两个矩形才会重叠
        return x_overlap and y_overlap