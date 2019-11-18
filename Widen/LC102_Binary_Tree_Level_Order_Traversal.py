"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# bfs using queue
# Runtime: 28 ms, faster than 98.75% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        level = [root.val]
        base_level = 0
        q = deque([[root, base_level+1]])
        while q:
            new_node_level = q.popleft()
            new_node, n_level = new_node_level[0], new_node_level[1]
            if n_level != base_level:
                res.append(level)
                level = []
                base_level = n_level
            if new_node.left:
                q.append([new_node.left, n_level+1])
                level.append(new_node.left.val)
            if new_node.right:
                q.append([new_node.right, n_level+1])
                level.append(new_node.right.val)
                
        return res
            