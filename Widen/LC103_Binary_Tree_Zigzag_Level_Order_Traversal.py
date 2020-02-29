"""
103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Runtime: 24 ms, faster than 96.10% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        deque = [[root, 1]]
        res_dict = collections.defaultdict(list)
        res_dict[1].append(root.val)
        while deque:
            node, depth = deque.pop(0)
            if node.left:
                deque.append([node.left, depth+1])
                res_dict[depth+1].append(node.left.val)
            if node.right:
                deque.append([node.right, depth+1])
                res_dict[depth+1].append(node.right.val)
        res = []
        for key in sorted(res_dict.keys()):
            if key % 2 == 1:
                res.append(res_dict[key])
            else:
                res.append(res_dict[key][::-1])
        return res
        
        