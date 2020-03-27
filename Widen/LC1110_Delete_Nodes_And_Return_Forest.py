"""
1110. Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""

# bfs, took 20min to finish
# Runtime: 60 ms, faster than 96.94% of Python3 online submissions for Delete Nodes And Return Forest.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = set([])
        res.add(root)
        deque = [root]
        while deque:
            node = deque.pop(0)
            if node.val in to_delete:
                if node in res:
                    res.remove(node)
                if node.left:
                    res.add(node.left)
                if node.right:
                    res.add(node.right)
                    
            if node.left:
                deque.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                deque.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
        return res