# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        x = 1
        head = prev
        # return head
        prev = None
        if n == 1:
            nxt = head.next
            head.next = None
            head = nxt
        while head:
            if x == n - 1:
                if head.next:
                    nxt = head.next.next
                else:
                    nxt = None
                head.next = prev
                prev = head
                head = nxt
            else:    
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            x += 1

        return prev
