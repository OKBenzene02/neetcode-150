class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def insert(self, node: Optional(Node)):
        prev = self.tail.prev
        nextt = self.tail

        prev.next = node
        node.prev = prev

        node.next = nextt
        nextt.prev = node
    
    def remove(self, node: Optional(Node)):
        prev = node.prev
        nextt = node.next
        prev.next = nextt
        nextt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.size:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
