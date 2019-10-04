'''
Time complexity: O(n),44 ms,82.86%
Space complexity: O(n),13.8 MB,5.24%
'''
#method1: recursion, DFS
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        temp_l = self.invertTree(root.left)
        temp_r = self.invertTree(root.right)
        root.right = temp_l
        root.left = temp_r
        return root

'''
Time complexity: O(n),48 ms,67.83%
Space complexity: O(n),13.8 MB,5.24%
'''
#method1: iteration, BFS
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        from collections import deque
        queue = deque()
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return root