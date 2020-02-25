"""
337. House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

# every time you met binary tree-related problem, do recursion
# Runtime: 44 ms, faster than 87.32% of Python3 online submissions for House Robber III.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for House Robber III.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        with_root_val, no_root_val = self.helper(root)
        return max(with_root_val, no_root_val)
    
    def helper(self, root):
        if root == None:
            return 0, 0 
        if root.left == None and root.right == None:
            return root.val, 0 
        with_left_root, no_left_root = self.helper(root.left)
        with_right_root, no_right_root = self.helper(root.right)
        with_root_val = root.val + no_left_root + no_right_root
        no_root_val = max(with_left_root, no_left_root) + max(with_right_root, no_right_root)
        
        return with_root_val, no_root_val
        
        