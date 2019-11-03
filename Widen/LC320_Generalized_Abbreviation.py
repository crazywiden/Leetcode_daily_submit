"""
LC320 -- Generalized Abbreviation
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""



# first backtracking by myself!
# although the efficiency is miserable
# Runtime: 552 ms, faster than 6.23% of Python3 online submissions for Generalized Abbreviation.
# Memory Usage: 22.2 MB, less than 100.00% of Python3 online submissions for Generalized Abbreviation.
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        if n == 0:
            return [""]
        if n == 1:
            return [word, "1"]
        # general all subset of the word
        subset = ["0", "1"]
        def helper(size, out):
            if size == 0:
                subset.extend(out)
            else:
                out1 = copy.deepcopy(out)
                for i in range(len(out1)):
                    out1[i] += "1"
                helper(size-1, out1)
                
                out2 = copy.deepcopy(out)
                for i in range(len(out2)):
                    out2[i] += "0"
                helper(size-1, out2)
        helper(n-1, subset.copy())
        subset = subset[2:]
        # generate words
        res = []
        for combination in subset:
            abbr_word = self.str2word(combination, word)
            res.append(abbr_word)
        return res
    
    def str2word(self, binary, word):
        res = ""
        cnt = 0
        if binary[0] == "0":
            res += word[0]
        else:
            cnt += 1
        for i in range(1, len(binary)):
            if binary[i] == "1":
                cnt += 1
            else:
                if cnt != 0:
                    res += str(cnt)
                res += word[i]
                cnt = 0
        if cnt != 0:
            res += str(cnt)
        return res


# backtracking with memo
# Runtime: 168 ms, faster than 91.39% of Python3 online submissions for Generalized Abbreviation.
# Memory Usage: 20.8 MB, less than 100.00% of Python3 online submissions for Generalized Abbreviation.
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        memo = collections.defaultdict(list)
        memo[''].append('')
        def dfs(word):
            if word in memo:
                return memo[word]
            
            for suf in dfs(word[1:]):
                memo[word].append(word[0] + suf)
            
            for i in range(1, len(word) + 1):
                for suf in dfs(word[i:]):
                    if not suf or suf[0] not in '123456789':
                        memo[word].append(str(i) + suf)
                        
            return memo[word]
        return dfs(word)

            