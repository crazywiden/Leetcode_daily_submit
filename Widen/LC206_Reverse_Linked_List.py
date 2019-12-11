"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""



# for most of linked list problem
# construct three pointers: prev, curr, nxt

# iteratively
# Runtime: 36 ms, faster than 78.94% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev, curr = None, head
        nxt = head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if not nxt:
                break
            nxt = nxt.next
        return prev



# recurisively
# Runtime: 32 ms, faster than 91.42% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 17.3 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next is None:
            return head
        next_p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next_p
