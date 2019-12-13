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

# method2 -- divide and conquer


