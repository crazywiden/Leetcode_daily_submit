# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# tutorial: https://leetcode.com/articles/merged-two-sorted-lists/
# recursion solution, more elegant
# Runtime: 28 ms, faster than 96.02% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if l2.val <= l1.val:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

# iteration solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = ListNode(-1)
        if l1.val <= l2.val:
            prev = l1
            l1 = l1.next
        else:
            prev = l2
            l2 = l2.next
        head.next = prev
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next 
            prev = prev.next 
        if l1 == None:
            prev.next = l2
        if l2 == None:
            prev.next = l1
        return head.next 
                
        