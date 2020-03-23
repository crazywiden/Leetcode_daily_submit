"""
958. Check Completeness of a Binary Tree
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
"""


# method1
# define a complete node as: has both left and right child
# for a complete binary tree, we can't have an incomplete node before a complete node 
# Runtime: 24 ms, faster than 98.76% of Python3 online submissions for Check Completeness of a Binary Tree.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Check Completeness of a Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        is_seen_incomplete = False
        queue = [root]
        while len(queue) > 0:
            tmp = queue.pop(0)
            if tmp.left != None:
                if is_seen_incomplete:
                    return False
                queue.append(tmp.left)
            else:
                is_seen_incomplete = True
                
            if tmp.right != None:
                if is_seen_incomplete:
                    return False
                queue.append(tmp.right)
            else:
                is_seen_incomplete = True
        return True
    
# method2
# for a complete binary tree, the number of node should be less than the index
# where the index of left child of each node should be 2*index + 1
#       the index of right child of each node should be 2*index + 2
# Runtime: 36 ms, faster than 42.91% of Python3 online submissions for Check Completeness of a Binary Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Check Completeness of a Binary Tree.
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        index = 0
        num_node = 0
        queue = [(root, index)]
        while queue:
            tmp, index = queue.pop(0)
            if tmp:
                num_node += 1 
                if index >= num_node:
                    return False
                queue.append((tmp.left, 2*index+1))
                queue.append((tmp.right, 2*index+2))
        return True
    