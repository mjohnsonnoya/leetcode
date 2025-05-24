# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
        else:
             head = list2

        while list1 and list2:
            if list1.val <= list2.val:
                while list1.next and list1.next.val <= list2.val:
                    list1 = list1.next
                nxt = list1.next
                list1.next = list2
                list1 = nxt
            else:
                while list2.next and list2.next.val < list1.val:
                    list2 = list2.next
                nxt = list2.next
                list2.next = list1
                list2 = nxt


        return head

        
        
