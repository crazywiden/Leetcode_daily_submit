"""
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Runtime: 88 ms, faster than 84.17% of Python3 online submissions for Reorder List.
# Memory Usage: 22 MB, less than 19.23% of Python3 online submissions for Reorder List.
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head
        n = 0
        counter = head
        while counter != None:
            n += 1
            counter = counter.next 
        
        backward_node = math.ceil(n/2 - 1)
        break_count = 0
        slow_p, fast_p = head, head
        while break_count < n - backward_node - 1:
            break_count += 1
            fast_p = fast_p.next
        fast_head = fast_p.next 
        fast_p.next = None
        fast_p = fast_head
        
        fast_p = self.reverse_list(fast_p)

        while fast_p != None:
            fast_nxt = fast_p.next 
            slow_nxt = slow_p.next
            slow_p.next = fast_p
            fast_p.next = slow_nxt
            slow_p = slow_nxt
            fast_p = fast_nxt
        return head
            
    def reverse_list(self, head):
        if head == None:
            return head
        prev, curr = None, head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
            
            
  
        