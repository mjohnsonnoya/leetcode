"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        dummy1 = head
        dummy2 = head
        while dummy1:
            hashmap[dummy1] = Node(dummy1.val)
            dummy1 = dummy1.next
        
        while dummy2:
            hashmap[dummy2].next = hashmap[dummy2.next]
            hashmap[dummy2].random = hashmap[dummy2.random]
            dummy2 = dummy2.next
        
        return hashmap[head]
