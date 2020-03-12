"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""
# first do inorder traverse
# then create the linked list
# but this kind of cheating? because I created a new list?
# Runtime: 32 ms, faster than 77.60% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # first do in-order tranverse
        # append all node into a list
        if root == None:
            return None
        all_node = self.in_order(root)
        # print(all_node)
        head = all_node[0]
        for i in range(len(all_node)-1):
            all_node[i].right = all_node[i+1]
            all_node[i+1].left = all_node[i]
        all_node[-1].right = all_node[0]
        all_node[0].left = all_node[-1]
        return head
    
    def in_order(self, root):
        if root == None:
            return []
        left_nodes = self.in_order(root.left)
        right_nodes = self.in_order(root.right)
        all_node = left_nodes + [root] + right_nodes
        return all_node


# this one seems more plausible, but actual solution should be morris algorithm
# Runtime: 64 ms, faster than 5.37% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        head = None
        prev, curr = None, None
        for node in self.in_order(root):
            if head == None:
                head = node
            curr = node
            if prev != None:
                curr.left = prev
                prev.right = curr
            prev = curr
        curr.right = head
        head.left = curr
        return head
    
    def in_order(self, root):
        if root == None:
            return
        for node in self.in_order(root.left):
            yield node
        yield root
        for node in self.in_order(root.right):
            yield node
            
    