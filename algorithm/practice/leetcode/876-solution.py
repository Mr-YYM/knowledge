"""
876. 链表的中间结点
https://leetcode-cn.com/problems/middle-of-the-linked-list/

问题描述:
给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

我的解题思路:
创建两个指针: 「快指针」和「慢指针」
「慢指针」向前一步，随后「快指针」向前两步。

解题过程遇到的问题:
判断条件 while fast and fast.next 为什么要这样


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list_node(node: ListNode):
    """
    可视化输出 ListNode
    """
    print('[', end='')
    prev = node
    while prev.next:
        print(prev.val, end=', ')
        prev = prev.next
    print(prev.val, end='')  # 别漏了最后一个数
    print(']')


def get_node(l: list):
    dummy_head = ListNode(None, None)
    prve = dummy_head
    for i in l:
        prve.next = ListNode(i, None)
        prve = prve.next
    
    return dummy_head.next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:  # ???
            slow = slow.next
            fast = fast.next.next
        
        return slow


demo_node = get_node([1,2,3,4,5,6])
result = Solution().middleNode(demo_node)
print_list_node(result)
