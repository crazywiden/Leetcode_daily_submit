# Definition for singly-linked list.
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Runtime: 24 ms, faster than 97.20% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        head_cnt, tail_cnt = 1, 1
        prev, curr = None, head
        nxt = head.next
        while head_cnt < m:
            curr, prev = nxt, curr
            nxt = nxt.next
            head_cnt = head_cnt + 1
            tail_cnt = tail_cnt + 1
            if nxt is None:
                break
        curr.next = prev
        while tail_cnt < n:
            tmp = nxt.next
            nxt.next = curr
            curr, nxt = nxt, tmp
            tail_cnt += 1  
        if prev:
            prev.next.next = nxt
            prev.next = curr
        else:
            head.next = nxt
            head = curr
        return head