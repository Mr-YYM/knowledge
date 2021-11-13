"""
102. 二叉树的层序遍历
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

题目描述:
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

"""
# Definition for a binary tree node.

from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        # 队列存储每个节点
        # 用队列可以保证层的顺序
        q = Queue()

        # 如果节点是空的话, 直接返回
        if not root:
            return result

        # 一开始，把 root 放进去
        q.put(root)

        # 不断从队列取值, 每走一轮 while, 就相当于进了一层
        while not q.empty():
            this_layer_nums = []

            this_layer_node_count = q.qsize()  # 此时队列有多少个元素, 就代表这个层级有多少个元素

            # 依次从队列取出它们
            for _ in range(this_layer_node_count):
                each_node = q.get()
                this_layer_nums.append(each_node.val)

                # 开始把下一层的元素丢进队列
                if each_node.left:
                    q.put(each_node.left)
                if each_node.right:
                    q.put(each_node.right)
            
            result.append(this_layer_nums)
        
        return result
