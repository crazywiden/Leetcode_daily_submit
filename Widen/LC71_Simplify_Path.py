"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
"""
# actually simple
# but need to figure out what does canonical path means
# Runtime: 24 ms, faster than 95.52% of Python3 online submissions for Simplify Path.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Simplify Path.
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elements = path.split("/")
        for ele in elements:
            if ele == "..":
                if stack:
                    stack.pop()
            elif ele == "." or ele == "":
                continue
            else:
                stack.append(ele)
        return "/" + "/".join(stack)