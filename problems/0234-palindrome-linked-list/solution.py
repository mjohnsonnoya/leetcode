# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        llist = []
        while head:
            llist.append(head.val)
            head = head.next

        l, r = 0, len(llist) - 1
        while l <= r:
            if llist[l] != llist[r]:
                return False
            l+=1
            r-=1
        return True
