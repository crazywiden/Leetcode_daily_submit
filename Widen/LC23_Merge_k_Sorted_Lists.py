"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""



# method1 -- using min heap
# time complexity -- O(nklogk)
# Runtime: 100 ms, faster than 88.88% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 16.6 MB, less than 42.42% of Python3 online submissions for Merge k Sorted Lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # method1 -- min heap
        n_list = len(lists)
        all_node = []
        for i in range(n_list):
            head = lists[i]
            while head:
                heapq.heappush(all_node, head.val)
                head = head.next
        head = ListNode(0)
        first = head
        while all_node:
            new_val = heapq.heappop(all_node)
            new_node = ListNode(new_val)
            first.next = new_node
            first = first.next
        return head.next


# merge2list
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        res = self.merge2lists(lists[0], lists[1])
        for i in range(2, len(lists)):
            new_l = lists[i]
            res = self.merge2lists(res, new_l)
        return res
    
    def merge2lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        res_head = res
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next 
            res = res.next 
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return res_head.next 



