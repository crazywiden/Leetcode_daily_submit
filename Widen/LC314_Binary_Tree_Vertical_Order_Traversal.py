"""
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
"""
# Runtime: 20 ms, faster than 99.71% of Python3 online submissions for Binary Tree Vertical Order Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Vertical Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # each node assign a location (depth, x)
        if root == None:
            return []
        stack = [[root, 1, 0]]
        res_dict = collections.defaultdict(list)
        res_dict[0].append(root.val)
        while stack:
            node, depth, idx = stack.pop(0)
            if node.left:
                stack.append([node.left, depth+1, idx-1])
                res_dict[idx-1].append(node.left.val)
            if node.right:
                stack.append([node.right, depth+1, idx+1])
                res_dict[idx+1].append(node.right.val)
        res = []
        for key in sorted(res_dict.keys()):
            res.append(res_dict[key])
        return res
    