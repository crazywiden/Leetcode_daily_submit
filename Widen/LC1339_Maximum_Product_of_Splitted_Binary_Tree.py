"""
1339. Maximum Product of Splitted Binary Tree
Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# method 1: first build a sum_tree, then iterative all sum node
# two pass dfs
# time complexity -- O(N)
# Runtime: 836 ms, faster than 5.09% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 81.6 MB, less than 17.78% of Python3 online submissions for Maximum Product of Splitted Binary Tree.

class NodeSum:
    def __init__(self, curr_sum=0, left_sum=0, right_sum=0, left=None, right=None):
        self.tot = curr_sum
        self.left_sum = left_sum
        self.right_sum = right_sum
        self.left = left
        self.right = right
        
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # each node get sum from left tree and sum from right tree
        MOD = 10**9 + 7
        sum_head = NodeSum()
        tot_sum = self.find_sum(root, sum_head)
        res = -1
        res = self.find_max(sum_head, res, tot_sum)
        return res % MOD
    
    def find_max(self, sum_root, max_val, tot_sum):
        take_left = (tot_sum - sum_root.left_sum) * sum_root.left_sum
        take_right = (tot_sum - sum_root.right_sum) * sum_root.right_sum
        max_val = max(max_val, take_left, take_right)
        if sum_root.left != None:
            left_max = self.find_max(sum_root.left, max_val, tot_sum)
            max_val = max(max_val, left_max)
        if sum_root.right != None:
            right_max = self.find_max(sum_root.right, max_val, tot_sum)
            max_val = max(max_val, right_max)
        return max_val         
        
    def find_sum(self, root, sum_node):
        sum_node.left = root.left
        sum_node.right = root.right
        if root.left == None:
            sum_node.left_sum = 0
        else:
            sum_node.left_sum = self.find_sum(root.left, sum_node.left)
        
        if root.right == None:
            sum_node.right_sum = 0
        else:
            sum_node.right_sum = self.find_sum(root.right, sum_node.right)
        
        sum_node.tot = sum_node.left_sum + sum_node.right_sum + root.val
        return sum_node.tot

    