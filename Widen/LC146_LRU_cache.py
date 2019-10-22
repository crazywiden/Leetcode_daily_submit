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
        self.hash_queue = {}
        self.head = -1
        self.tail = -1
        self.len = 0
    
    def update_to_end(self, key):
        # update previous node and post node
        if self.hash_queue[key][1] != -1:
            prev = self.hash_queue[key][1]
            self.hash_queue[prev][2] = self.hash_queue[key][2]
        if self.hash_queue[key][2] != -1:
            post = self.hash_queue[key][2]
            self.hash_queue[post][1] = self.hash_queue[key][1]
            
        self.hash_queue[self.tail][2] = key
        self.hash_queue[key][1] = self.tail
        self.head = self.hash_queue[key][2]
        self.hash_queue[key][2] = -1
        self.tail = key
        
        
    def get(self, key: int) -> int:
        if key not in self.hash_queue:
            return -1
        
        if key == self.tail:
            return self.hash_queue[key][0]
        
        self.update_to_end(key)
        return self.hash_queue[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_queue:
            self.hash_queue[key][0] = value
            if self.hash_queue[key][2] != -1:
                self.update_to_end(key)
        else:
            if self.len >= self.capacity:
                first_ele = self.hash_queue.pop(self.head)
                second_ele = first_ele[2]
                if second_ele != -1:
                    self.hash_queue[second_ele][1] = -1
                self.head = second_ele
                self.len -= 1
            if self.len == 0:
            	self.tail = -1
            
            self.hash_queue[key] = [value, -1, -1]
            self.hash_queue[key][1] = self.tail
            if self.tail != -1:
                self.hash_queue[self.tail][2] = key
            else:
                self.head = key
            self.tail = key
            self.len += 1
        
            
            

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(1)
cache.put(2, 1)
cache.get(2)
print(cache.hash_queue, cache.head, cache.tail)
cache.put(3, 2)
cache.get(2)
cache.get(3)





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

