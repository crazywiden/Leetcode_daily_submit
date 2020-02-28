"""
480. Sliding Window Median
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""

# implemetation of hashheap
# I am so south...
# Runtime: 812 ms, faster than 22.18% of Python3 online submissions for Sliding Window Median.
# Memory Usage: 15.2 MB, less than 20.00% of Python3 online submissions for Sliding Window Median.
class HashHeap:
    def __init__(self, min_heap=True):
        self.heap = [] # each ele is a tuple, the first ele is the val, the second is the key
        self.hash_dict = {}  # use key as key, use index in self.heap as value
        self.is_min = min_heap
        
    @property
    def size(self):
        return len(self.heap)
        
    def top(self):
        val = self.heap[0][0]
        key = self.heap[0][1]
        return key, val
    
    def _swap(self, key1, key2):
        index1 = self.hash_dict[key1]
        index2 = self.hash_dict[key2]
        val1 = self.heap[index1]
        val2 = self.heap[index2]
        
        self.hash_dict[key1] = index2
        self.hash_dict[key2] = index1
        self.heap[index1] = val2
        self.heap[index2] = val1 
    
    def pop(self):
        assert self.size > 0, "size is zero, can't pop"
        val = self.heap[0][0]
        key = self.heap[0][1]
        self.remove(key)
        return key, val
    
    def push(self, key, val):
        self.heap.append((val, key))
        self.hash_dict[key] = self.size - 1 
        self._shift_up(key)
    
    def remove(self, key):
        last_key = self.heap[-1][1]
        self._swap(key, last_key)
        self.hash_dict.pop(key)
        self.heap.pop()
        if key != last_key:
            self._shift_down(last_key)
            self._shift_up(last_key)

    def _shift_up(self, key):
        index = self.hash_dict[key]
        parent = (index - 1) // 2
        parent_key = self.heap[parent][1]
        while parent >= 0 and self.is_less(index, parent):
            self._swap(key, parent_key)
            index = self.hash_dict[key]
            parent = (index - 1) // 2
            parent_key = self.heap[parent][1]
        
    def _shift_down(self, key):
        index = self.hash_dict[key]
        left = index * 2 + 1 
        right = index * 2 + 2 
        min_idx = index
        if left < self.size and self.is_less(left, min_idx):
            min_idx = left 
        if right < self.size and self.is_less(right, min_idx):
            min_idx = right
        
        while index != min_idx:
            min_key = self.heap[min_idx][1]
            self._swap(key, min_key)
            index = self.hash_dict[key]
            left = index * 2 + 1 
            right = index * 2 + 2 
            min_idx = index 
            if left < self.size and self.is_less(left, min_idx):
                min_idx = left 
            if right < self.size and self.is_less(right, min_idx):
                min_idx = right

    def is_less(self, idx1, idx2):
        val1 = self.heap[idx1][0]
        val2 = self.heap[idx2][0]
        if self.is_min:
            return val1 < val2 
        else:
            return val1 > val2
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) == 0:
            return []
        max_heap = HashHeap(min_heap=False)
        min_heap = HashHeap(min_heap=True)
        thres = (k + 1) // 2
        is_even = k%2 == 0
        res = []
        for i in range(k):
            max_heap.push(i, nums[i])
            if max_heap.size > thres:
                key, val = max_heap.pop()
                min_heap.push(key, val)
        
        if is_even:
            _, val1 = max_heap.top()
            _, val2 = min_heap.top()
            res.append((val1+val2)/2)
        else:
            key, val = max_heap.top()
            res.append(val)
        # print(min_heap.heap, max_heap.heap)
        for i in range(k, len(nums)):
            if nums[i] < max_heap.top()[1]:
                max_heap.push(i, nums[i])
            else:
                min_heap.push(i, nums[i])
            
            if i-k in max_heap.hash_dict:
                max_heap.remove(i-k)
            if i-k in min_heap.hash_dict:
                min_heap.remove(i-k)
            
            if max_heap.size > thres:
                key, val = max_heap.pop()
                min_heap.push(key, val)
            if min_heap.size > k-thres:
                key, val = min_heap.pop()
                max_heap.push(key, val)
                
            if is_even:
                _, val1 = max_heap.top()
                _, val2 = min_heap.top()
                res.append((val1+val2)/2)
            else:
                key, val = max_heap.top()
                res.append(val)
            # print(min_heap.heap, max_heap.heap)
        return res 
    
    