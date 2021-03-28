class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(float('inf'), float('inf'))
        self.tail = Node(float('-inf'), float('-inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_at_head(self, node):
        tmp_next = self.head.next
        self.head.next = node
        node.next = tmp_next
        node.prev = self.head
        tmp_next.prev = node

    def delete_node(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
    
    def delete_from_tail(self):
        key = self.tail.prev.key
        self.delete_node(self.tail.prev)
        return key
    
class LRUCache:

    def __init__(self, capacity: int):
        self.node_map = defaultdict(Node)
        self.capacity = capacity
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.list.delete_node(node)
            self.list.insert_at_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.node_map:
            node = Node(key, value)
            self.node_map[key] = node
            self.list.insert_at_head(node)
            if len(self.node_map) == self.capacity + 1:
                key = self.list.delete_from_tail()
                del self.node_map[key]
        else:#update
            self.list.delete_node(self.node_map[key])
            node = Node(key, value)
            self.node_map[key] = node
            self.list.insert_at_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
