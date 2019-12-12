"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Runtime: 60 ms, faster than 97.42% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p, q = l1, l2
        dummy_head = ListNode(0)
        curr = dummy_head
        while p or q:
            if p:
                l1_val = p.val
            else:
                l1_val = 0
                
            if q:
                l2_val = q.val
            else:
                l2_val = 0
            
            digit = carry + l1_val + l2_val
            carry = digit // 10
            curr.next = ListNode(digit%10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next
            
            
            
            
            
            
            
                    
        