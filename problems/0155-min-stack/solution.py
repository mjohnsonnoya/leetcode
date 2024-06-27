class Node:

    def __init__(self, val = None, m = None, n = None):
        self.val = val
        self.min = m
        self.next = n

class MinStack:

    def __init__(self):
        self.head = Node()
        # self.min = float('inf')

        

    def push(self, val: int) -> None:
        if not self.head.next: 
            item = Node(val, m = val, n = None)
            self.head.next = item
        else:
            item = Node(val, m = min(self.head.next.min, val), n = self.head.next)
            self.head.next = item
        

    def pop(self) -> None:
        self.head.next = self.head.next.next
        

    def top(self) -> int:
        return self.head.next.val
        

    def getMin(self) -> int:
        return self.head.next.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
