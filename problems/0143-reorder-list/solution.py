# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            h_nxt = head.next
            p_nxt = prev.next
            head.next = prev
            if h_nxt != prev:
                prev.next = h_nxt
            prev = p_nxt
            head = h_nxt
        

        
