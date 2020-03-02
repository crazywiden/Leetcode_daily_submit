"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    @property
    def size(self):
        return len(self.min_heap) + len(self.max_heap)
    
    def addNum(self, num: int) -> None:
        if len(self.max_heap) > 0 and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
            
        if len(self.max_heap) > len(self.min_heap) + 1:
            ele = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -ele)
        if len(self.min_heap) > len(self.max_heap):
            ele = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -ele)
    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0])/2
        return -self.max_heap[0] 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()