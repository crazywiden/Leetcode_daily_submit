"""
272. Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""



# maintain two stacks to use loop to implement dfs 
# time complexity -- O(logN)
# soooo smart!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack)
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
        
        result = []
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
                
        return result
        
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return stack
        
    def move_upper(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
                
    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
            
        if not upper_stack:
            return True
            
        return target - lower_stack[-1].val < upper_stack[-1].val - target