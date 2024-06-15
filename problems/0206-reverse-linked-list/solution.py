# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def recursive(node):
            if not node.next:
                return node
            new_head = recursive(node.next)
            node.next.next = node
            node.next = None
            return new_head

        return recursive(head)

