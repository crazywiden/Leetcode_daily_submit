'''
Time complexity: O(n),52 ms, 98.04%
Space complexity: O(n)?,16.3 MB, 5.10%
'''
#method1: DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dists_l = []

    def dists(self, root: TreeNode):
        [root_left, root_right] = [0, 0]
        if root.left:
            root_left = max(self.dists(root.left)) + 1
        if root.right:
            root_right = max(self.dists(root.right)) + 1
        self.dists_l.append([root_left, root_right])
        return [root_left, root_right]

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dists_l = []
        if not root or ((not root.left) and (not root.right)): return 0
        self.dists(root)
        res_l = 0
        for i in self.dists_l:
            res_l = max(sum(i), res_l)
        return res_l