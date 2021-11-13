"""
111. 二叉树的最小深度
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

题目描述:
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
"""
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        q = Queue()
        q.put(root)
        
        while not q.empty():
            
            this_layer_node_count = q.qsize()  # 此时队列有多少个元素, 就代表这个层级有多少个元素

            # 遍历这一层的每个 TreeNode
            for _ in range(this_layer_node_count):
                each_node = q.get()

                # 都是空的，就可以返回了
                if not each_node.left and not each_node.right:
                    return count
                
                if each_node.left:
                    q.put(each_node.left)
                
                if each_node.right:
                    q.put(each_node.right)

            count += 1

        return count
