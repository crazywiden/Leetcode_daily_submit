"""
LC105 -- Construct Binary Tree from Preorder and Inorder Traversal
This quesition was asked in ThoughtSpot screen interview
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


this problem is classic and thus relatively easy
However, the challenge is how to speed up
"""

# method 1 -- just normal recursion
# Runtime: 216 ms, faster than 22.87% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88.6 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        left_node_preorder = preorder[1:idx+1]
        left_node_inorder = inorder[:idx]
        left_node = self.buildTree(left_node_preorder, left_node_inorder)
        
        right_node_preorder = preorder[idx+1:]
        right_node_inorder = inorder[idx+1:]
        right_node = self.buildTree(right_node_preorder, right_node_inorder)
        
        root.left = left_node
        root.right = right_node
        return root



# method 2 
# used two tricks:
# 1. use hash map to speed up search efficiency
# 2. use iter/next to simplify code

class Solution(object):
    def buildTree(self, preorder, inorder):
        l = len(inorder)
        inor_dict = {i:idx for idx, i in enumerate(inorder)}
        pre_iter = iter(preorder)
        
        def helper(start, end):
            if start > end: 
                return None
            num = next(pre_iter)
            root = TreeNode(num)
            idx = inor_dict[num]
            root.left = helper(start, idx)
            root.right = helper(idx+1, end)
        return helper(0, l-1)



# method3 --  use dictionary to speed up, non-recursion version
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(0)
        lo, hi = 0, len(preorder) - 1
        nodes = [(root, lo, hi)]
        lut = {inorder[i]: i for i in range(len(inorder))}
        # use a look up table to get the index
        # of an element in constant time.
        for i in range(len(preorder)):
            curr, lo, hi = nodes.pop()
            curr.val = preorder[i]
            mid = lut[curr.val]
            if mid < hi:
                curr.right = TreeNode(0)
                nodes.append((curr.right, mid + 1, hi))
            if lo < mid:
                curr.left = TreeNode(0)
                nodes.append((curr.left, lo, mid - 1))
        return root
