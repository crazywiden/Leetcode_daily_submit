"""
LC210 Course schedule
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
"""
# topological sort
# Runtime: 116 ms, faster than 30.44% of Python3 online submissions for Course Schedule II.
# Memory Usage: 14.1 MB, less than 96.43% of Python3 online submissions for Course Schedule II.
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        courses = collections.defaultdict(list)
        res = []
        in_degree = [0 for _ in range(n)]
        
        for i in range(len(prerequisites)):
            father = prerequisites[i][1]
            child = prerequisites[i][0]
            courses[father].append(child)
            in_degree[child] += 1
        
        q = []
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        
        while len(q) != 0:
            new_node = q.pop()
            res.append(new_node)
            for child in courses[new_node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
        if len(res) != n:
            return []
        return res
    
    