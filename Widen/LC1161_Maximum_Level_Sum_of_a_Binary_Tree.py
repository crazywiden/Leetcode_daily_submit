"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level bfs
# Runtime: 332 ms, faster than 52.30% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 18 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_level, max_sum = -1, -1
        deque = [root]
        curr_level = 0
        while deque:
            tmp = deque.copy()
            deque = []
            curr_sum = 0 
            curr_level += 1
            while tmp:
                node = tmp.pop(0)
                curr_sum += node.val
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            if curr_sum > max_sum:
                max_level = curr_level
                max_sum = curr_sum
        return max_level
    
                    
                