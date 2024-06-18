class Node:

    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cache = {}
    
    def add(self, node):
        self.head.next.prev = node      
        node.next = self.head.next  
        self.head.next = node
        node.prev = self.head

    def remove(self, node):
        nxt = node.next
        nxt.prev = node.prev
        node.prev.next = nxt
        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
