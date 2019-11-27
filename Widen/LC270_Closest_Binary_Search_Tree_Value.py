"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Runtime: 40 ms, faster than 86.28% of Python3 online submissions for Closest Binary Search Tree Value.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Closest Binary Search Tree Value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float("inf")
        curr_res = root.val
        while root:
            if diff > abs(root.val - target):
                diff = abs(root.val - target)
                curr_res = root.val
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        return curr_res