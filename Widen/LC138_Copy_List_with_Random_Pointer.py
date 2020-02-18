"""
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
"""

# Runtime: 28 ms, faster than 94.68% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def get_clone_node(self, node):
        if node == None:
            return None
        if node in self.visited_node:
            return self.visited_node[node]
        new_node = Node(node.val, None, None)
        self.visited_node[node] = new_node
        return new_node
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        self.visited_node = {}
        
        new_node = Node(head.val, None, None)
        old_node = head
        self.visited_node[head] = new_node
        while old_node != None:
            new_node.next = self.get_clone_node(old_node.next)
            new_node.random = self.get_clone_node(old_node.random)
            
            new_node = new_node.next
            old_node = old_node.next
            
        return self.visited_node[head]
    
        