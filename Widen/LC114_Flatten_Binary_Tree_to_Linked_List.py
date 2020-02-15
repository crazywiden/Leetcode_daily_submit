"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Runtime: 32 ms, faster than 86.54% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 13.6 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        if root.left == None and root.right == None:
            return root 
    
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left == None:
            return root 
        
        left = root.left 
        prev = root.left 
        nxt = prev.right
        while nxt != None:
            prev = nxt
            nxt = nxt.right 
        
        prev.right = root.right 
        root.right = left 
        root.left = None
        