"""
LC 24 swap nodes in pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Runtime: 24 ms, faster than 91.85% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        prev = None
        left, right = head, head.next
        
        res = head.next 
        while right != None:
            nxt = right.next 
            right.next = left 
            left.next = nxt 
            if prev != None:
                prev.next = right 
            prev = left
            left = nxt
            if nxt is None:
                break
            right = nxt.next 
            
            
        return res
            