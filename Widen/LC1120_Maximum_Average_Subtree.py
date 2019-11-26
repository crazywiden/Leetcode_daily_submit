"""
1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

"""

# recursive
# Runtime: 52 ms, faster than 89.85% of Python3 online submissions for Maximum Average Subtree.
# Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for Maximum Average Subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = float("-inf")
        self.tranverse_subtrees(root)
        return self.res
    
    def tranverse_subtrees(self, root):
        if root == None:
            return [0, 0]
        left_n, left_val = self.tranverse_subtrees(root.left)
        right_n, right_val = self.tranverse_subtrees(root.right)
        sub_res = (left_n*left_val + right_n*right_val + root.val) / (left_n+right_n+1)
        self.res = max(self.res, sub_res)
        return [left_n+right_n+1, sub_res]


            