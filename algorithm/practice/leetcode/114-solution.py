"""
114. 二叉树展开为链表
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

问题描述:
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # 左右两边 flatten
        self.flatten(root.left)
        self.flatten(root.right)

        # 右子树先存下来
        right = root.right
        # 右子树改为已经 flatten 好的左子树
        root.right = root.left
        root.left = None

        # 遍历到右子树的末尾, 把刚刚存下来的原先的右子树贴上去
        p = root
        while p.right:
            p = p.right
        p.right = right
