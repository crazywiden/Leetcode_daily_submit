#reference：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
'''
Time complexity: O(n+m), 48 ms, 92.99%
Space complexity: O(n), 13.9 MB, 5.66%
'''
#method linked list
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next

        if l1 is None:
            prev.next = l2
        else:
            prev.next = l1
        return prehead.next




