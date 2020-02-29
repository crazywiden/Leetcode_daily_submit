"""
199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# binay tree problem and linkedList problem are always easy
# Runtime: 28 ms, faster than 81.64% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Right Side View.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        view = [root.val]
        left_view = self.rightSideView(root.left)
        right_view = self.rightSideView(root.right)
        if len(left_view) > len(right_view):
            right_view = right_view + left_view[len(right_view):]
        return view + right_view
    