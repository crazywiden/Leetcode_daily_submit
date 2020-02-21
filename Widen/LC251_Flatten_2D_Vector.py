"""
251. Flatten 2D Vector
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
"""


# Runtime: 68 ms, faster than 100.00% of Python3 online submissions for Flatten 2D Vector.
# Memory Usage: 18.4 MB, less than 100.00% of Python3 online submissions for Flatten 2D Vector.
class Vector2D:
    def __init__(self, vec2d):
        self.vec = []
        for ele in vec2d:
            self.vec.extend(ele)
        

    # @return {int} a next element
    def next(self):
        return self.vec.pop(0)
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return len(self.vec) > 0
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()