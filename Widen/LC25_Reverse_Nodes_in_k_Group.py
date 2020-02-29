"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Runtime: 48 ms, faster than 74.88% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reverse Nodes in k-Group.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fix_head = ListNode(0)
        fix_head.next = head
        
        cnt = 1
        prev, curr = fix_head, head
        prev_tail = fix_head
        while curr != None:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1
            if cnt > k:
                curr_tail = prev_tail.next
                prev_tail.next = prev
                prev_tail = curr_tail
                prev = curr_tail
                prev.next = curr
                cnt = 1
        prev, curr = curr, prev
        while cnt > 1:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt -= 1
            
        return fix_head.next 
                
                
            
            