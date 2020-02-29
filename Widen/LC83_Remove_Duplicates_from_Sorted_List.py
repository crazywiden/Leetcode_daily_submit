"""
83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# feels so good to do easy problem
# Runtime: 40 ms, faster than 70.86% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        all_val = set([])
        all_val.add(head.val)
        prev, curr = head, head.next
        while curr != None:
            if curr.val not in all_val:
                all_val.add(curr.val)
                curr = curr.next 
                prev = prev.next
                continue
            nxt = curr.next
            prev.next = nxt
            curr = nxt
        return head 

# take advantage of sorted attribute
# Runtime: 36 ms, faster than 90.42% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev, curr = head, head.next
        while curr != None:
            if prev.val == curr.val:
                curr = curr.next
                prev.next = curr 
            else:
                curr = curr.next 
                prev = prev.next 
        return head
        
    