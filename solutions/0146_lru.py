class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node: Node):
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
