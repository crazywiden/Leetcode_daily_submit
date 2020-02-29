"""
160. Intersection of Two Linked Lists

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# first get difference between two linked list
# then let the longer list start first to make two list equal size
# Runtime: 172 ms, faster than 38.86% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = self.get_len(headA)
        len_B = self.get_len(headB)
        if len_A == 0 or len_B == 0:
            return None
        p_A, p_B = headA, headB
        if len_A > len_B:
            while len_A > len_B:
                p_A = p_A.next
                len_A -= 1
        else:
            while len_B > len_A:
                p_B = p_B.next 
                len_B -= 1
        
        while p_A != None and p_B != None:
            if p_A == p_B:
                return p_A
            p_A = p_A.next 
            p_B = p_B.next 
        return None
    
    def get_len(self, root):
        tmp = root
        cnt = 0
        while tmp != None:
            tmp = tmp.next 
            cnt += 1 
        return cnt