# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = ListNode()
        dummy = curr

        carry = 0
        while l1 or l2 or carry:
            curr.next = ListNode()
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            x = l1_val + l2_val + carry

            curr.next.val = x % 10
            carry = x // 10
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
            
            
