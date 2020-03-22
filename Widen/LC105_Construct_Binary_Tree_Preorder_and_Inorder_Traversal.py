"""
LC105 -- Construct Binary Tree from Preorder and Inorder Traversal
This quesition was asked in ThoughtSpot screen interview
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


this problem is classic and thus relatively easy
However, the challenge is how to speed up
"""
# optimized using hashmap
# Runtime: 56 ms, faster than 89.74% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 17.8 MB, less than 86.84% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder_idx = {val:idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        return self.helper(preorder, 0, n, inorder, 0, n)

    def helper(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start >= pre_end or in_start >= in_end:
            return None
        head = TreeNode(preorder[pre_start])
        root_idx = self.inorder_idx[preorder[pre_start]]
        left_len = root_idx - in_start
        right_len = in_end - root_idx
        
        left_tree = self.helper(preorder, pre_start+1, pre_start+1+left_len, inorder, in_start, root_idx)
        right_tree = self.helper(preorder, pre_start+1+left_len, pre_end, inorder, root_idx+1, in_end)
        
        head.left = left_tree
        head.right = right_tree
        return head
    
# used the number of element in each tree to separate left tree and right tree
# Runtime: 444 ms, faster than 8.37% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88.3 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # can also make use of the number of elements
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_idx = i
                break
        num_left = root_idx
        num_right = len(inorder) - root_idx
        left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx+1:]
        left_preorder, right_preorder = preorder[1:1+root_idx], preorder[root_idx+1:]
        left_tree = self.buildTree(left_preorder, left_inorder)
        right_tree = self.buildTree(right_preorder, right_inorder)
        root.left = left_tree
        root.right = right_tree
        return root
    

            
        
# used hash map to separate the left tree and right tree in pre-order tranversal
# Runtime: 456 ms, faster than 7.81% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_idx = i
                break
    
        if root_idx == 0:
            left_tree = None
            right_preorder = preorder[1:] 
            right_inorder = inorder[1:]
            right_tree = self.buildTree(right_preorder, right_inorder) 
        elif root_idx == len(inorder) - 1:
            right_tree = None
            left_preorder = preorder[1:]
            left_inorder = inorder[:-1]
            left_tree = self.buildTree(left_preorder, left_inorder)
        else:
            left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx+1:]
            left_ele = set(left_inorder)
            for i in range(1, len(preorder)):
                if preorder[i] not in left_ele:
                    left_preorder, right_preorder = preorder[1:i], preorder[i:]
                    break

            left_tree = self.buildTree(left_preorder, left_inorder)
            right_tree = self.buildTree(right_preorder, right_inorder)    
        
        root.left = left_tree
        root.right = right_tree
        return root
        
# method 1 -- just normal recursion
# Runtime: 216 ms, faster than 22.87% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88.6 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         n = len(preorder)
#         if n == 0:
#             return None
#         if n == 1:
#             return TreeNode(preorder[0])
        
#         root = TreeNode(preorder[0])
#         idx = inorder.index(preorder[0])
        
#         left_node_preorder = preorder[1:idx+1]
#         left_node_inorder = inorder[:idx]
#         left_node = self.buildTree(left_node_preorder, left_node_inorder)
        
#         right_node_preorder = preorder[idx+1:]
#         right_node_inorder = inorder[idx+1:]
#         right_node = self.buildTree(right_node_preorder, right_node_inorder)
        
#         root.left = left_node
#         root.right = right_node
#         return root



# method 2 
# used two tricks:
# 1. use hash map to speed up search efficiency
# 2. use iter/next to simplify code
# Runtime: 36 ms, faster than 99.98% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

class Solution:
    def buildTree(self, preorder, inorder):
        idx = {i:idx for idx, i in enumerate(inorder)}
        n = len(preorder)
        p = 0
        def helper(start, end):
            nonlocal p
            if start > end or p == n:
                return None
            root = TreeNode(preorder[p])
            mid = idx[preorder[p]]
            print(preorder[p])
            p += 1
            root.left = helper(start, mid-1)
            root.right = helper(mid+1, end)
            return root
        return helper(0, n-1)

sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol.buildTree(preorder, inorder)


# # method3 --  use dictionary to speed up, non-recursion version
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder) == 0:
#             return None
#         root = TreeNode(0)
#         lo, hi = 0, len(preorder) - 1
#         nodes = [(root, lo, hi)]
#         lut = {inorder[i]: i for i in range(len(inorder))}
#         # use a look up table to get the index
#         # of an element in constant time.
#         for i in range(len(preorder)):
#             curr, lo, hi = nodes.pop()
#             curr.val = preorder[i]
#             mid = lut[curr.val]
#             if mid < hi:
#                 curr.right = TreeNode(0)
#                 nodes.append((curr.right, mid + 1, hi))
#             if lo < mid:
#                 curr.left = TreeNode(0)
#                 nodes.append((curr.left, lo, mid - 1))
#         return root
