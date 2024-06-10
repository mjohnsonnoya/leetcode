# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while True:
            if not head:
                return False
            visited.add(head)
            if head.next in visited:
                return True
            else:
                head = head.next
