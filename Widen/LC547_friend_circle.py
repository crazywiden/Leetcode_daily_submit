"""
LC 547 -- Friend Circle
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""

# solution 1: UnionFindSet
# Runtime: 224 ms, faster than 63.76% of Python3 online submissions for Friend Circles.
# Memory Usage: 13.8 MB, less than 41.18% of Python3 online submissions for Friend Circles.
class UnionFindSet():
    def __init__(self, x):
        self.val = x
        self.parent = x

def find_set(x):
    if x.parent == x.val:
        return x
    if isinstance(x.parent, int):
    	return x

    return find_set(x.parent)

class Solution:
    def findCircleNum(self, M) -> int:
        N = len(M)
        cnt = N
        all_student = [UnionFindSet(i) for i in range(1, N+1)]
        for i in range(N):
            parent1 = find_set(all_student[i])
            for j in range(i+1, N):
                if M[i][j] == 1:
                    parent2 = find_set(all_student[j])
                    if parent2 != parent1:
                        parent2.parent = parent1
                        cnt -= 1
        return cnt
                

# method2: dfs
# for each student, add their name to visited list
# return how many group have been visited
class Solution:
    def visit(self, i, M, visited):
        p = M[i]
        visited[i] = 1
        for j in range(len(M)):
            if p[j] == 1 and visited[j] == 0:
                self.visit(j, M, visited)
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        count = 0
        visited = [0] * n
        for i in range(n):
            if visited[i] == 1:
                continue
            count += 1
            self.visit(i, M, visited)
        return count







