class Solution:
    """
    投影法解题
    """
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if not (rec1[2] > rec1[0] and rec1[3] > rec1[1]):
            return False
        if not (rec2[2] > rec2[0] and rec2[3] > rec2[1]):
            return False
        x_overlap = not (rec2[0] >= rec1[2] or rec2[2] <= rec1[0])
        y_overlap = not (rec2[1] >= rec1[3] or rec2[3] <= rec1[1])
        return x_overlap and y_overlap