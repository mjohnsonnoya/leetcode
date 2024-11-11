# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            prev_sorted = dummy
            next_current = curr.next
            while prev_sorted.next and prev_sorted.next.val <= curr.val:
                prev_sorted = prev_sorted.next

            curr.next = prev_sorted.next
            prev_sorted.next = curr

            curr = next_current
        
        return dummy.next




            
