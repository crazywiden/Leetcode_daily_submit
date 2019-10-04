"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
"""
# met this problem in a interview of ThoughtSpot
# topological sorting -- use of stack
# time complexity -- O(V+E), V is number of vertices and E is the number of edges
# Runtime: 44 ms, faster than 44.37% of Python3 online submissions for Alien Dictionary.
# Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Alien Dictionary.
# class Solution:
#     def alienOrder(self, words) -> str:
#         # edges -- matrix
#         # edges[i][j] means vertice[i]
        
#         # build graph
#         all_letter = set()
#         dependency = []
#         n = len(words)
#         letter_pos = {0:[words[0][0]]}
#         for word in words:
#             if word[0] not in letter_pos[0]: # we meet a new word start
#                 letter_pos[0].append(word[0])
#                 dependency.append(letter_pos)
#                 letter_pos = {0:[word[0]]}

#             for j in range(len(word)):
#                 if word[j] not in all_letter:
#                     all_letter.add(word[j])
#                 if j in letter_pos:
#                     if word[j] not in letter_pos[j]:
#                         letter_pos[j].append(word[j])
#                 else:
#                     letter_pos[j] = [word[j]]
#         dependency.append(letter_pos)

        
#         letter_idx = {idx:letter for idx, letter in enumerate(all_letter)}
#         all_letter = {letter:idx for idx, letter in enumerate(all_letter)}
#         n = len(all_letter)
#         letter_graph = [[0 for _ in range(n)] for _ in range(n)]
        
#         for dependency_dict in dependency:
#             for key, val in dependency_dict.items():
#                 base_idx = all_letter[val[0]]
#                 for i in range(1, len(val)):
#                     child_idx = all_letter[val[i]]
#                     letter_graph[base_idx][child_idx] = 1

#         # letter_graph[i][j] == 1 means letter[i] is parent of letter[j]
        
#         # start topological sort
#         letter_state = [False for _ in range(n)]
#         letter_order = []

#         def helper(node):
#             if all(letter_state):
#                 return
            
#             if letter_state[node] == True: # visited this node
#                 return 

#             letter_state[node] = True

#             if sum(letter_graph[node]) == 0: # no children
#                 letter_order.append(letter_idx[node])
#             else:
#                 for i in range(n):
#                     if letter_graph[node][i] == 1:
#                         helper(i)
#                 letter_order.append(letter_idx[node])

#         for i in range(n):
#             if not letter_state[i]:
#                 helper(i)

#         return "".join(letter_order[::-1])


# class Solution:
#     def alienOrder(self, words) -> str:
#         # Find ancestors of each node by DFS.
#         nodes, ancestors = set(), {}
#         for i in range(len(words)):
#             for c in words[i]:
#                 nodes.add(c)
#         for node in nodes:
#             ancestors[node] = []
#         for i in range(1, len(words)):
#             if len(words[i-1]) > len(words[i]) and \
#                 words[i-1][:len(words[i])] == words[i]:
#                     return ""
#             self.findEdges(words[i - 1], words[i], ancestors)

#         # Output topological order by DFS.
#         result = []
#         visited = {}
#         for node in nodes:
#             if self.topSortDFS(node, node, ancestors, visited, result):
#                 return ""

#         return "".join(result)


#     # Construct the graph.
#     def findEdges(self, word1, word2, ancestors):
#         min_len = min(len(word1), len(word2))
#         for i in range(min_len):
#             if word1[i] != word2[i]:
#                 ancestors[word2[i]].append(word1[i])
#                 break


#     # Topological sort, return whether there is a cycle.
#     def topSortDFS(self, root, node, ancestors, visited, result):
#         if node not in visited:
#             visited[node] = root
#             for ancestor in ancestors[node]:
#                 if self.topSortDFS(root, ancestor, ancestors, visited, result):
#                     return True
#             result.append(node)
#         elif visited[node] == root:
#             # Visited from the same root in the DFS path.
#             # So it is cyclic.
#             return True
#         return False
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}
        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)
         
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and \
                words[i-1][:len(words[i])] == words[i]:
                    return ""
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)
         
        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)
         
        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)
             
            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
             
                del out_degree[precedence]
         
        if out_degree:
            return ""
 
        return "".join(result)
 
 
    # Construct the graph.
    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in range(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break

if __name__ == '__main__':
    sol = Solution()
    # words = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"] # expected is ""
    words = ["wrt","wrf","er","ett","rftt","te"]

    print(sol.alienOrder(words))
                
        
        
        


