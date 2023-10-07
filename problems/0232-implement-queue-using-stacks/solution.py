class Node:
    
    def __init__(self, val, prev = None , next = None):
        self.val = val
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
        
class MyQueue:

    def __init__(self):
        self.my_queue = DoubleLinkedList()

    def push(self, x: int) -> None:
        if self.empty():
            self.my_queue.tail = self.my_queue.head = Node(x)
        else:
            self.my_queue.tail.next = Node(x)
            self.my_queue.tail.next.prev = self.my_queue.tail
            self.my_queue.tail = self.my_queue.tail.next
            

    def pop(self) -> int:
        if self.empty():
            pass
        else:
            val = self.my_queue.head.val
            self.my_queue.head = self.my_queue.head.next
            if not self.my_queue.head:
                self.my_queue.tail = None
            else:
                self.my_queue.head.prev = None
        return val

    def peek(self) -> int:
        if self.empty():
            pass
        else:
            val = self.my_queue.head.val
            return val
        

    def empty(self) -> bool:
        if not self.my_queue.head:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
