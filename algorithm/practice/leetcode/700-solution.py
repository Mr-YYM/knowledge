r"""
700. 二叉搜索树中的搜索
https://leetcode-cn.com/problems/search-in-a-binary-search-tree/

给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 
返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2     
     / \   
    1   3

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 这句话别漏了
        if not root:
            return None

        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        
        if root.val > val:
            return self.searchBST(root.left, val)
