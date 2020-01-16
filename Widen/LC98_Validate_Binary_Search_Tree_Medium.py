"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# recursion method
# Runtime: 44 ms, faster than 61.82% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, lower=-float("inf"), upper=float("inf"))
    
    def helper(self, root, lower, upper):
        if root is None:
            return True
        val = root.val
        if not (lower < val and val < upper):
            return False
        if not self.helper(root.left, lower, val):
            return False
        if not self.helper(root.right, val, upper):
            return False
        return True



# use stack to do the iteration rather than recursion
# Runtime: 40 ms, faster than 84.88% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack = [[root, -float("inf"), float("inf")]]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= upper:
                return False
            stack.append([root.right, root.val, upper])
            stack.append([root.left, lower, root.val])
        return True



# use inorder traversal
# the idea here is we don't need to traverse all the element
# only need to compare the last one and the current root value 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        last_val = float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= last_val:
                return False
            last_val = root.val
            root = root.right
            
        return True
    
    
    
    


















