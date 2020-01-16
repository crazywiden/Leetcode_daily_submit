"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# recursive
# Runtime: 20 ms, faster than 96.69% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        res = left + [root.val] + right
        return res


# iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right 
        return inorder






