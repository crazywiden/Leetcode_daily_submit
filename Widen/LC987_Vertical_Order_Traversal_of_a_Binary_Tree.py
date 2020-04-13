"""
987. Vertical Order Traversal of a Binary Tree
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""

# Runtime: 20 ms, faster than 99.80% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 14.2 MB, less than 33.33% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        tot_level = collections.defaultdict(list)
        deque = [[root, 0, 0]]
        while deque:
            node, level, depth = deque.pop()
            tot_level[level].append([node.val, depth])
            if node.left != None:
                deque.append([node.left, level-1, depth+1])
            if node.right != None:
                deque.append([node.right, level+1, depth+1])
        
        res = []
        for key in sorted(tot_level.keys()):
            nodes = sorted(tot_level[key], key=lambda x:(x[1], x[0]))
            res.append([val for val, _ in nodes])
        return res
    