"""
"""



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# iterative solution
# Runtime: 28 ms, faster than 76.04% of Python3 online submissions for Nested List Weight Sum.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Nested List Weight Sum.
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        level = 1
        return self.helper(nestedList, level)
    def helper(self, nestedList, level):
        res = 0
        for ele in nestedList:
            if ele.isInteger():
                res += ele.getInteger() * level
            else:
                tmp = self.helper(ele.getList(), level+1)
                res += tmp
        return res



# Runtime: 28 ms, faster than 76.04% of Python3 online submissions for Nested List Weight Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Nested List Weight Sum.
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        stack = []
        for ele in nestedList:
            stack.append((ele, 1))
        
        while len(stack) > 0:
            ele, level = stack.pop(0)
            if ele.isInteger():
                res += ele.getInteger() * level
            else:
                for i in ele.getList():
                    stack.append((i, level+1))
        return res
        