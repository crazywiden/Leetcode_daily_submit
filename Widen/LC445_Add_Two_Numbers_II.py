"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# should be more familiar 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        # self.print_list(l1)
        # self.print_list(l2)
        flag = False
        res = ListNode(0)
        res_head = res
        while l1 != None and l2 !=None:
            tmp = l1.val + l2.val
            if flag:
                tmp += 1 
                flag = False
            if tmp >= 10:
                flag = True
            nxt_node = ListNode(tmp%10)
            res.next = nxt_node
            res = nxt_node
            l1 = l1.next
            l2 = l2.next
        # print("iii")
        # self.print_list(res)
        flag = self.append_rest(l1, res, flag)
        flag = self.append_rest(l2, res, flag)
        # print("kkk")
        # self.print_list(res)
        while res.next != None:
            res = res.next 
        if flag:
            res.next = ListNode(1)
        
        return self.reverse(res_head.next)
    
    def reverse(self, root):
        prev, curr = None, root
        while curr != None:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def append_rest(self, l1, res, flag):
        while l1 != None:            
            tmp = l1.val 
            if flag:
                tmp +=1 
                flag = False
            if tmp >= 10:
                flag = True
            nxt_node = ListNode(tmp%10)
            res.next = nxt_node
            l1 = l1.next 
            res = nxt_node
        return flag
        # print("00")
        # self.print_list(res)
            
    def print_list(self, root):
        res = []
        while root != None:
            res.append(root.val)
            root = root.next 
        print(res)
