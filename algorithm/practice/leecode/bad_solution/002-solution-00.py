# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        dummy_head = ListNode(None, self)
        result = ''
        while dummy_head.next is not None:
            result += f'{dummy_head.next.val}->'
            dummy_head = dummy_head.next
        
        return result

class Solution:
    @staticmethod
    def get_list_length(list_node: ListNode):
        """
        获取链表长度
        """
        length = 1
        head: ListNode = list_node

        while head.next is not None:
            length += 1
            head = head.next
        
        return length

    def get_sorted_list_group(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        按长度排序两个链表
        """
        l1_length = self.get_list_length(l1)
        l2_length = self.get_list_length(l2)
        if l1_length >= l2_length:
            return l1, l2
        else:
            return l2, l1


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        loggest_list_group = self.get_sorted_list_group(l1, l2)
        a_list = loggest_list_group[0]
        b_list = loggest_list_group[1]

        dummy_a_head: ListNode = ListNode(None, a_list)
        dummy_b_head: ListNode = ListNode(None, b_list)

        dummy_result_list: ListNode = ListNode(None, None)
        dummy_result_head: ListNode = dummy_result_list
        carry = 0
        # 遍历最长的那个链表
        while dummy_a_head.next is not None:
            dummy_a_head = dummy_a_head.next
            if dummy_b_head.next is not None:
                dummy_b_head = dummy_b_head.next
                added_val = dummy_a_head.val + dummy_b_head.val + carry
            else:
                added_val = dummy_a_head.val + carry

            new_node_val = added_val % 10
            carry = int(added_val / 10)  # 进位
            dummy_result_head.next = ListNode(new_node_val, None)
            dummy_result_head = dummy_result_head.next
        
        # 最后还要判断一次进位
        if carry:
            dummy_result_head.next = ListNode(carry, None)
        
        return dummy_result_list.next
