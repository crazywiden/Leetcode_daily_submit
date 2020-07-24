"""

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.
"""

# topological sort
"""
Runtime: 284 ms, faster than 81.69% of Python3 online submissions for Parallel Courses.
Memory Usage: 16.3 MB, less than 64.71% of Python3 online submissions for Parallel Courses.
"""
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indegree = [0 for _ in range(N+1)]
        graph = collections.defaultdict(list)
        for pre, nxt in relations:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        deque = []
        step = 1
        for i in range(N):
            if indegree[i] == 0:
                deque.append([i, step])
     
        while deque:
            course, step = deque.pop(0)
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    deque.append([child, step+1])
        for i in range(N):
            if indegree[i] != 0:
                return -1
        return step
        
            