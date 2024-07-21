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
        mapping = {}
        g = head
        h = head
        if not head: return None
        while g:
            mapping[g] = Node(g.val)
            g = g.next
        while h:
            if h.next:
                mapping[h].next = mapping[h.next]
            if h.random:
                mapping[h].random = mapping[h.random]
            h = h.next
        return mapping[head]

        

        

