"""
460. LFU 缓存
https://leetcode-cn.com/problems/lfu-cache/

请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

    - LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
    - int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
    - void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。
      当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。
      在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
      注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

"""
from typing import Dict


class Node:
    """
    双链表节点
    """
    def __init__(self, key: int, val: int, prev: "Node"=None, next: "Node"=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    """
    双链表实现
    """
    def __init__(self) -> None:
        # 大小
        self.size = 0

        # 初始化头尾两个节点
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # 头尾接起来
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_last(self, node: Node):
        """
        在末尾添加元素
        """
        # 原理就是把元素放在 tail 前面
        # 单看很难懂，这里手动画一下图比较好理解

        node.next = self.tail
        node.prev = self.tail.prev
        # tail 前面的元素的 next 接上 node
        self.tail.prev.next = node
        # 最后把 tail 的 prev 接上 node
        self.tail.prev = node

        self.size += 1

    def remove(self, node: Node):
        """
        删除 node， 这个 node 一定存在， node 引用直接指向它
        """
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
    
    def remove_first(self) -> Node:
        """
        最前面代表最老的那个
        """
        if self.size == 0:
            return
        
        first_node = self.head.next
        self.remove(first_node)
        
        return first_node


class LinkedHashSet:
    """
    哈希链表的实现
    """
    def __init__(self) -> None:
        self.cache = DoubleLinkedList()
        self.map = {}

    def add(self, key: int):
        node = Node(key, 0)
        self.cache.add_last(node)
        self.map[key] = node
    
    def remove(self, key: int):
        node = self.map[key]
        self.cache.remove(node)
        self.map.pop(key)
    
    def remove_least_recently(self) -> int:
        """
        删除最久没有使用
        """
        deleted_node = self.cache.remove_first()
        node_key = deleted_node.key
        self.map.pop(node_key)

        return node_key

    def is_empty(self):
        return len(self.map) == 0


class LFUCache:
    """
    
    """

    def __init__(self, capacity: int):
        self.key_val = {}  # KV 表
        self.key_freq = {}  # KF 表
        self.freq_keys: Dict[int, LinkedHashSet] = {}  # FK 表。用于找到 freq 最小的 key
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        
        self.increaseFreq(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <=0:
            return
        
        # 如果存在
        if key in self.key_val:
            self.key_val[key] = value  # 修改
            self.increaseFreq(key)  # 频次修改
            return
        
        # 如果不存在
        # 检查是否满了
        if len(self.key_val) >= self.capacity:
            self.remove_min_freq_key()
        
        self.key_val[key] = value
        self.key_freq[key] = 1
        if 1 not in self.freq_keys:
            self.freq_keys[1] = LinkedHashSet()
        self.freq_keys[1].add(key)  # 对应频次的元素
        self.min_freq = 1

    def increaseFreq(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] = freq + 1

        # 将 key 从 freq 对应列表删除
        self.freq_keys[freq].remove(key)
        # 加到 freq + 1 表里
        if freq+1 not in self.freq_keys:
            self.freq_keys[freq+1] = LinkedHashSet()
        self.freq_keys[freq+1].add(key)

        if self.freq_keys[freq].is_empty():
            self.freq_keys.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1

    def remove_min_freq_key(self):
        """
        去掉频次最低的 key
        """
        key_list = self.freq_keys[self.min_freq]  # 拿到最小频次的哈希链表
        to_delete_key = key_list.remove_least_recently()  # 删除最老的那个
        if key_list.is_empty:
            self.freq_keys.pop(self.min_freq)  # 空了，就不需要了
        
        self.key_val.pop(to_delete_key)
        self.key_freq.pop(to_delete_key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)