"""
281. Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.

 

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
"""


# Runtime: 104 ms, faster than 5.14% of Python3 online submissions for Zigzag Iterator.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Zigzag Iterator.
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.is_first = True
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        if len(self.v1) == 0:
            self.is_first = False
        if len(self.v2) == 0:
            self.is_first = True
            
        if self.is_first:
            self.is_first = False
            return self.v1.pop(0)
            
        else:
            self.is_first = True
            return self.v2.pop(0)
            
        

    def hasNext(self) -> bool:
        return len(self.v1) > 0 or len(self.v2) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
