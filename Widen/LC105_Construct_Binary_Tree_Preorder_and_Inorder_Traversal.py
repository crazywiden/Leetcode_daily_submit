"""
LC105 -- Construct Binary Tree from Preorder and Inorder Traversal
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



# method 2 --  use dictionary to speed up
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pindex2index = {x:i for i, x in enumerate(inorder)}
        self.pindex = 0
        return self.helper(preorder, inorder, 0, len(preorder) - 1, pindex2index)
    
    def helper(self, preorder, inorder, start, end, mapping):
        if start > end:
            return None
        
        to_ret = TreeNode(preorder[self.pindex])
        
        old_pindex = self.pindex
        
        
        left_start, left_end = start, mapping[preorder[old_pindex]] - 1
        if left_start <= left_end:
            self.pindex += 1
            to_ret.left = self.helper(preorder, inorder,
                                      left_start, left_end, mapping)
        else:
            to_ret.left = None
        
        right_start, right_end = mapping[preorder[old_pindex]] + 1, end
        
        if right_start <= right_end:
            self.pindex += 1
            to_ret.right = self.helper(preorder, inorder,
                                   right_start, right_end, mapping)
        else:
            to_ret.right = None
        
        return to_ret



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
