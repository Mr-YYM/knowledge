"""
146. LRU 缓存机制
https://leetcode-cn.com/problems/lru-cache/

问题描述:
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；
如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 
进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？


"""

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
        if self.size == 0:
            return
        
        first_node = self.head.next
        self.remove(first_node)
        
        return first_node



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoubleLinkedList()
        self.map = {}
    
    # 封装一些函数，操作 cache 和 map， 避免删除的时候忘记把 map 上的应用去掉

    def make_recently(self, key: int):
        node = self.map[key]
        self.cache.remove(node)
        self.cache.add_last(node)

    def add_recently(self, key: int, val: int):
        node = Node(key, val)
        self.cache.add_last(node)
        self.map[key] = node
    
    def delete_key(self, key: int):
        node = self.map[key]
        self.cache.remove(node)
        self.map.pop(key)
    
    def remove_least_recently(self):
        """
        删除最久没有使用
        """
        deleted_node = self.cache.remove_first()
        node_key = deleted_node.key
        self.map.pop(node_key)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.make_recently(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        # 如果存在，则更新
        if key in self.map:
            self.delete_key(key)
            self.add_recently(key, value)
            return
        
        # 达到容量上限就清理
        if self.cache.size == self.capacity:
            self.remove_least_recently()
        
        self.add_recently(key, value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)