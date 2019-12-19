"""
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""



# time complexity --O(N)
# the method to update the value of each node is really clever
# update a global variable `self.res`, while return another value
# in this way we can preserve the larger one
# Runtime: 92 ms, faster than 78.79% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 19.5 MB, less than 100.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        max_with_root = self.sub_tree(root)
        return max(self.res, max_with_root)
    
    def sub_tree(self, root):
        if root == None:
            return 0
        # if root.left == None and root.right == None:
        #     return root.val
        
        left_max = self.sub_tree(root.left)
        right_max = self.sub_tree(root.right)
        # print("left_max", left_max, is_use_left)
        # print("right_max", right_max, is_use_right)
        new_val = root.val + max(left_max, 0) + max(right_max, 0)
        self.res = max(self.res, new_val)
        return root.val + max(left_max, right_max, 0)
        