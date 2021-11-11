r"""
226. 翻转二叉树
https://leetcode-cn.com/problems/invert-binary-tree/

翻转一棵二叉树。
示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

解题思路:
递归调用，交换左右节点

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 退出条件
        if not root:
            return
        
        # 交换左右节点
        temp = root.left
        root.left = root.right
        root.right = temp

        # 继续替换
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
