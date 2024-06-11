# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while True:
            if not slow or not fast:
                return False
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if slow == fast:
                return True
