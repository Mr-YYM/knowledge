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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_a_head: ListNode = ListNode(None, l1)
        dummy_b_head: ListNode = ListNode(None, l2)

        dummy_result_list: ListNode = ListNode(None, None)
        dummy_result_head: ListNode = dummy_result_list
        carry = 0

        while dummy_a_head.next is not None or dummy_b_head.next is not None:
            dummy_a_head = dummy_a_head.next
            dummy_b_head = dummy_b_head.next
            added_val = dummy_a_head.val + dummy_b_head.val + carry
            
            added_val = dummy_a_head.val + carry
            added_val = dummy_b_head.val + carry

            new_node_val = added_val % 10
            carry = int(added_val / 10)  # 进位
            dummy_result_head.next = ListNode(new_node_val, None)
            dummy_result_head = dummy_result_head.next
        
        # 最后还要判断一次进位
        if carry:
            dummy_result_head.next = ListNode(carry, None)
        
        return dummy_result_list.next

a = ListNode(1, None)
b = ListNode(2, a)
c = ListNode(3, b)

r = Solution().addTwoNumbers(c, c)
print(r)