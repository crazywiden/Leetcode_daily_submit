"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# recursion version
# Runtime: 32 ms, faster than 96.82% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 14.5 MB, less than 93.75% of Python3 online submissions for Maximum Depth of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# non-recursion version
# Runtime: 44 ms, faster than 34.25% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Depth of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        depth = 1
        stack = [(root, depth)]
        while len(stack) > 0:
            node, curr_depth = stack.pop()
            if node != None:
                depth = max(curr_depth, depth)
                stack.append((node.left, curr_depth+1))
                stack.append((node.right, curr_depth+1))
        return depth