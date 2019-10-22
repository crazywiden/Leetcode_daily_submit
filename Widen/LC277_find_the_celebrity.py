"""
LC 277 -- Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""



# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


# method 1 -- most straight forward thinking...
# Runtime: 1572 ms, faster than 26.04% of Python online submissions for Find the Celebrity.
# Memory Usage: 12 MB, less than 26.67% of Python online submissions for Find the Celebrity.
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        relation = set()  # each element is a tuple, meaning i knows j
        for i in range(n):
            celebrity = i
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):  # i know j, so i can't be the one
                    celebrity = -1
                    relation.add((i, j))
                    break
            if celebrity != -1:  # meaning i knows nobody
                for k in range(n):
                    if k == celebrity:
                        continue
                    if not knows(k, celebrity):  # exists someone doesn't know celebrity
                        celebrity = -1
                        break
            if celebrity != -1:
                return celebrity
        return -1
                        

# method 2 -- reference :https://www.cnblogs.com/grandyang/p/5310649.html
# soooo smart!! why can't I think of this
# Runtime: 1152 ms, faster than 97.52% of Python online submissions for Find the Celebrity.
# Memory Usage: 11.9 MB, less than 43.33% of Python online submissions for Find the Celebrity.

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(n):
            if knows(res, i):
                res = i
        for i in range(res):
            if (knows(res, i)) or (not knows(i, res)):
                return -1
        for i in range(res+1, n):
            if (not knows(i, res)):
                return -1
        return res
                        
        
        