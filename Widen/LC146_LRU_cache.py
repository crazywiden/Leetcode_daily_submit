"""
LC146 LRU cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key is key
        # value is at tuple. value[0] -- value, value[1] -- prev key, value[2] -- post key
        self.hash = dict()
        self.head = -1
        self.tail = -1
        self.len = 0

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        ele = self.hash[key]
        prev, post = ele[1], ele[2]
        
        if prev != -1:
            self.hash[prev][2] = post
        if post != -1:
            self.hash[post][1] = prev
            
        self.hash[key][1] = self.tail
        self.hash[key][2] = -1
        return ele[0]

    def put(self, key: int, value: int) -> None:
        if self.len >= self.capacity:
            head = self.hash.pop(self.head)
            self.head = head[2]
            self.len -= 1
        if key not in self.hash:
            self.hash[key] = [-1, -1, -1]
            
        self.hash[key][0] = value
        self.hash[key][1] = self.tail
        self.hash[key][2] = -1
        self.tail = key
        if self.len == 0:
            self.head = key
        if key not in self.hash:
            self.len += 1

            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.hash, obj.head, obj.tail)
print(obj.get(1))
print(obj.hash, obj.head, obj.tail)
obj.put(3,3)
print(obj.hash, obj.head, obj.tail)
obj.put(4,4)
print(obj.hash, obj.head, obj.tail)
obj.get(1)
print(obj.hash, obj.head, obj.tail)
print(obj.get(3))
print(obj.get(4))




# method 2 -- turns out there is a OrderedDict() in collections package...
# Runtime: 204 ms, faster than 92.62% of Python3 online submissions for LRU Cache.
# Memory Usage: 22.4 MB, less than 6.06% of Python3 online submissions for LRU Cache.

import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

