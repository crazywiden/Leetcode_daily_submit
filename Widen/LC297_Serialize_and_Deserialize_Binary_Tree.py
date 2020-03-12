"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# serialize and de-serialize using layer traverse
# bfs
# Runtime: 108 ms, faster than 95.13% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        deque = [root]
        res = [root.val]
        while deque:
            node = deque.pop(0)
            if node.left:
                deque.append(node.left)
                res.append(node.left.val)
            else:
                res.append(None)
            if node.right:
                deque.append(node.right)
                res.append(node.right.val)
            else:
                res.append(None)
        # print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        head = TreeNode(data[0])
        curr = head
        deque = [curr]
        val_idx = 1
        while deque:
            curr_node = deque.pop(0)
            if data[val_idx] == None:
                curr_node.left = None
            else:
                curr_node.left = TreeNode(data[val_idx])
                deque.append(curr_node.left)
            val_idx += 1
            
            if data[val_idx] == None:
                curr_node.right = None
            else:
                curr_node.right = TreeNode(data[val_idx])
                deque.append(curr_node.right)
            val_idx += 1
        return head
                

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))