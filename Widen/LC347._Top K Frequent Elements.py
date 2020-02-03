"""
347. Top K Frequent Elements
"""

# this question is relatively easy
# key idea was to build a hash map and a heap
# to create map between value and requency
# the reason why I post this question here because the offical solution is so elegant


# official solution:
# Runtime: 100 ms, faster than 91.93% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 17.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
# my solution:
# Runtime: 104 ms, faster than 78.45% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 17.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        for i, item in enumerate(sorted(freq.items(), key=lambda x:x[1], reverse=True)):
            res.append(item[0])
            if i == k-1:
                return res
            
        