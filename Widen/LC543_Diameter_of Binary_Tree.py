"""
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# actually took me a while
# Runtime: 44 ms, faster than 67.62% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth, left_span = self.maxDepth(root.left)
        right_depth, right_span = self.maxDepth(root.right)
        return max(left_depth + right_depth, left_span, right_span)
    
    def maxDepth(self, root):
        if root == None:
            return 0, 0
        left_depth, left_span = self.maxDepth(root.left)
        right_depth, right_span = self.maxDepth(root.right)
        depth = 1 + max(left_depth, right_depth)
        span = max(left_depth + right_depth, left_span, right_span)
        return depth, span