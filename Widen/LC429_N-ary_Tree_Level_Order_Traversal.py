"""
LC429 N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
"""



# Runtime: 664 ms, faster than 78.75% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 96.8 MB, less than 8.33% of Python3 online submissions for N-ary Tree Level Order Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        level = [root.val]
        base_level = 0
        q = deque([[root, base_level+1]])
        while q:
            new_node_level = q.popleft()
            new_node, new_level = new_node_level[0], new_node_level[1]
            if new_level != base_level:
                res.append(level)
                base_level = new_level
                level = []
            for child in new_node.children:
                level.append(child.val)
                q.append([child, new_level+1])
        return res






                