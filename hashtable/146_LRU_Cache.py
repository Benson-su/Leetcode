class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.cache = DoubleLinkedList()

    def get(self, key):
        # 判断 key 是否存在，分情况处理
        if key not in self.hashmap:
            return -1
        # 通过哈希表定位其在双向链表的位置
        value = self.hashmap[key].value
        # 这里实现的逻辑在 put 操作体现
        # put 操作在键存在时，同样需要移至链表头部
        self.put(key, value)
        return value

    def put(self, key, value):
        # 先创建节点
        node = Node(key, value)
        # 同样判断 key 是否存在
        # 分情况处理
        if key in self.hashmap:
            self.cache.remove_node(self.hashmap[key])
            self.cache.add_to_head(node)
            self.hashmap[key] = node
        else:
            # 判断缓存容量是否不够
            if self.capacity == self.cache.get_size():
                # 删除最后的节点
                tail = self.cache.remove_tail()
                self.hashmap.pop(tail.key)
            # 添加到头部
            self.cache.add_to_head(node)
            self.hashmap[key] = node

class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_to_head(self, node):
        """添加节点到头部
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove_node(self, node):
        """删除节点
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_tail(self):
        """删除尾部节点
        """
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node
    
    def get_size(self):
        return self.size





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
