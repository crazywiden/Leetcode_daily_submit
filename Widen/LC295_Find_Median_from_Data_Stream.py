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



# data structure is binary search
# add time complexity -- O(logN)
# calculate media time complexity -- O(1)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sorted_arr = []
        self.len = 0

    def addNum(self, num: int) -> None:
        left, right = 0, self.len
        if self.len == 0:
            self.sorted_arr.append(num)
        elif self.sorted_arr[-1] <= num:
            self.sorted_arr.append(num)
        elif self.sorted_arr[0] >= num:
            self.sorted_arr.insert(0, num)
        else:
            idx = self.find_idx(left, right, num)
            self.sorted_arr.insert(idx+1, num)
        self.len += 1
        

    def findMedian(self) -> float:
        if self.len % 2 != 0:
            return self.sorted_arr[self.len//2]
        else:
            right = self.len // 2
            left = right - 1
            return (self.sorted_arr[right] + self.sorted_arr[left])/2
    
    def find_idx(self, left, right, ele):
        if self.len == 0:
            return 0
        
        while left < right:
            mid = (left + right) // 2
            if self.sorted_arr[mid] > ele:
                right = mid - 1 
            elif self.sorted_arr[mid] < ele:
                left = mid + 1
            else:
                return mid
        if self.sorted_arr[left] < ele:
            return left
        return left - 1
              
# two heaps





        
        