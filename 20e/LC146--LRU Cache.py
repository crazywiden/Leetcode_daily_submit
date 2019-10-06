'''
Time complexity: O(n),out of limit
Space complexity: O(n)
'''
#method 1:
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict ={}
        self.use ={}

    def get(self, key: int) -> int:
        if key in self.dict:
            self.use[key]=max(self.use.values())+1
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if (key not in self.dict) and self.cap > 0 :
            self.dict[key]=value
            if not self.use:
                self.use[key]=1
            else:
                self.use[key]=max(self.use.values())+1
            self.cap=self.cap-1
        elif (key not in self.dict) and self.cap == 0:
            a = [rm for rm,v in self.use.items() if v == min(self.use.values())]
            self.dict.pop(a[0])
            self.use.pop(a[0])
            self.dict[key]=value
            if not self.use:
                self.use[key]=1
            else:
                self.use[key]=max(self.use.values())+1
        elif key in self.dict:
            self.dict[key]=value
            self.use[key]=max(self.use.values())+1


'''
Time complexity: O(1),308 ms, 42.57%
Space complexity: O(n), 23.1 MB, 5.64%
'''
#method2: Hashtable+Linkedlist(queue)
#reference:https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new

'''
Time complexity: O(1),292 ms, 48.93%
Space complexity: O(n), 22.8 MB, 5.64%
'''
#method3: LinkedDict
#reference:https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)