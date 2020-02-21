"""
173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
"""


# Runtime: 76 ms, faster than 73.23% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 19.9 MB, less than 69.23% of Python3 online submissions for Binary Search Tree Iterator.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.sorted_num = self.inorder(root)
    
    def inorder(self, root):
        if root == None:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left + [root.val] + right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.sorted_num) > 0:
            return self.sorted_num.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.sorted_num) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# stack method
# Runtime: 80 ms, faster than 51.12% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 19.9 MB, less than 69.23% of Python3 online submissions for Binary Search Tree Iterator.
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left 

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack[-1]
        if node.right != None:
            tmp = node.right
            while tmp != None:
                self.stack.append(tmp)
                tmp = tmp.left
        else:
            tmp = self.stack.pop()
            while len(self.stack) > 0 and self.stack[-1].right == tmp:
                tmp = self.stack.pop()
        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



