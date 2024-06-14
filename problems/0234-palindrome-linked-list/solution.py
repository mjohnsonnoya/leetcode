# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast and not fast.next:
            slow = slow.next

        
        prev = None
        while slow:
            fut = slow.next
            slow.next = prev
            prev = slow
            slow = fut

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        
        
        
