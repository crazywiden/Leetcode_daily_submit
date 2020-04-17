"""
545. Boundary of Binary Tree
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
"""

# deal with left boundary, right boundary, lower bounday respectively
# Runtime: 40 ms, faster than 88.77% of Python3 online submissions for Boundary of Binary Tree.
# Memory Usage: 15.4 MB, less than 71.43% of Python3 online submissions for Boundary of Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        # find left boundary
        left_boundary = []
        prev, curr = root, root.left
        while curr != None:
            left_boundary.append(prev.val)
            prev = curr
            if curr.left != None:    
                curr = curr.left
            else:
                curr = curr.right 
        if len(left_boundary) == 0:
            left_boundary = [root.val]
            
        # find right boundary
        right_boundary = []
        prev, curr = root, root.right 
        while curr != None:
            right_boundary.append(prev.val)
            prev = curr
            if curr.right != None:
                curr = curr.right 
            else:
                curr = curr.left 
        if len(right_boundary) == 0:
            right_boundary = [root.val]
        right_boundary = right_boundary[::-1]
        # find lower boundary using dfs
        lower_boundary = self.get_leaves(root)
        return [root.val] + left_boundary[1:] + lower_boundary + right_boundary[:-1]

    def get_leaves(self, root):
        if root.left == None and root.right == None:
            return [root.val]
        res = []
        if root.left != None:
            left_part = self.get_leaves(root.left)
            res += left_part
        if root.right != None:
            right_part = self.get_leaves(root.right)
            res += right_part
        return res
    
            
    
    
    
    
    
    