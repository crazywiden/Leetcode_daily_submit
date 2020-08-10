"""
109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# simple
# pretty much everything related with Tree is simple
# time complexity -- O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return self.helper(l)
    
    def helper(self, l):
        if len(l) == 0:
            return None
        if len(l) == 1:
            return TreeNode(val=l[0])
        mid = len(l)//2
        root = TreeNode(val=l[mid])
        root.left = self.helper(l[:mid])
        root.right = self.helper(l[mid+1:])
        return root
    