"""
LC411 Minimum Unique word abbreviation
A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""

# combined the result of two: LC320. Generalized Abbreviation(use dp) and LC408. Valid Word Abbreviation(O(N))
# TLE however
import collections
import heapq
import re
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # first find all possible abbreviation in target
        # using dfs with memory
        memo = collections.defaultdict(list)
        memo[""].append("")
        def dfs(word):
            if word in memo:
                return memo[word]
            # keep the first letter
            for suf in dfs(word[1:]):
                memo[word].append(word[0] + suf)
                
            # use the first few letter as abbreviation
            for i in range(1, len(word) + 1):
                for suf in dfs(word[i:]):
                    if (not suf) or (suf[0] not in "1234567890"):
                        memo[word].append(str(i) + suf)
            return memo[word]
        target_abbr = dfs(target)
        target_heap = []
        for i in range(len(target_abbr)):
            tmp_abbr = target_abbr[i]
            heapq.heappush(target_heap, (len(tmp_abbr), tmp_abbr))
        if len(dictionary) == 0:
            return heapq.heappop(target_heap)[1]
        is_match = False
        while len(target_heap)!=0 and (not is_match):
            tmp_res = heapq.heappop(target_heap)
            for i in range(len(dictionary)):
                if self.check_match(tmp_res[1], dictionary[i]):
                    is_match = False
                    break
                is_match = True
        if is_match:
            return tmp_res[1]
        
    def check_match(self, abbr, word):
        abbr_char = re.findall("[a-z]+", abbr)
        abbr_digit = re.findall("[0-9]+", abbr)
        if abbr[0] >= "0" and abbr[0] <= "9":
            if int(abbr_digit[0]) > len(word):
                return False
            if abbr[0][0] == "0":
                return False
            return self.compare(word[int(abbr_digit[0]):], abbr_char, abbr_digit[1:])
        else:
            return self.compare(word, abbr_char, abbr_digit)
    
    def compare(self, word, abbr_char, abbr_digit):
        start = 0
        if len(abbr_char) == 0 and len(word) != 0:
            return False
        while start < len(word):
            if len(abbr_char) != 0:
                tmp_seg = abbr_char.pop(0)
                if word[start:start+len(tmp_seg)] != tmp_seg:
                    return False
                start = start + len(tmp_seg)
            if len(abbr_digit) != 0:
                tmp_abbr = abbr_digit.pop(0)
                if tmp_abbr[0] == "0":
                    return False
                start += int(tmp_abbr)
            if len(abbr_char) == 0 and len(abbr_digit) == 0:
                break
        if len(abbr_char) == 0 and len(abbr_digit) == 0 and start == len(word):
            return True
        else:
            return False

# if add two more important pruning, it will pass
import collections
import re
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # first find all possible abbreviation in target
        # using dfs with memory
        if len(dictionary) == 0:
            return str(len(target))
        dictionary = [d for d in dictionary if len(d) == len(target)]
        
        memo = collections.defaultdict(list)
        memo[""].append("")
        def dfs(word):
            if word in memo:
                return memo[word]
            # keep the first letter
            for suf in dfs(word[1:]):
                memo[word].append(word[0] + suf)
                
            # use the first few letter as abbreviation
            for i in range(1, len(word) + 1):
                for suf in dfs(word[i:]):
                    if (not suf) or (suf[0] not in "1234567890"):
                        memo[word].append(str(i) + suf)
            return memo[word]
        target_abbr = dfs(target)
    
        target_heap = [(len(abbr), abbr) for abbr in target_abbr]
        target_heap = sorted(target_heap, key=lambda x:(x[0], x[1]))
        
        if len(dictionary) == 0:
            return target_heap[0][1]
        is_match = False
        while len(target_heap)!=0 and (not is_match):
            tmp_res = target_heap.pop(0)
            for i in range(len(dictionary)):
                if self.check_match(tmp_res[1], dictionary[i]):
                    is_match = False
                    break
                is_match = True
        if is_match:
            return tmp_res[1]
        
    def check_match(self, abbr, word):
        w = 0
        a = 0
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit() and abbr[a] != '0':
                e = a
                while e < len(abbr) and abbr[e].isdigit(): e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            else:
                if word[w] != abbr[a]:
                    return False

                w += 1
                a += 1

        return w == len(word) and a == len(abbr)
        
# new method
# Runtime: 388 ms, faster than 38.78% of Python3 online submissions for Minimum Unique Word Abbreviation.
# Memory Usage: 26.9 MB, less than 100.00% of Python3 online submissions for Minimum Unique Word Abbreviation.
import collections
import re
class Solution:
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def checkWord(word, dictionary, l):
            # return if a word in valid according to the dictionary
            for check_word in dictionary:
                if l!=len(check_word):
                    continue
                i=0
                for element in abbr_word:
                    if type(element)==int: # a number indicates some str, just skip.
                        i += element
                    else:
                        if element != check_word[i]:
                            break # not match, continue to the next check_word
                        i += 1
                if i==l:
                    return False # match! not valid!
            return True # valid
        
        # 0. filter the dictionary
        l = len(target)
        dictionary = [d for d in dictionary if len(d)==l]
        if not dictionary: 
        	return str(l)
        
        # 1. list all the abbreviations
        abbr = [] # store all the abbr.
        for i in range(2**l):
            # bin(i) denotes an abbr.
            t = bin(i)[2:].zfill(l) # abbr in string format
            j = 0
            abbr_word = [] # a formatted abbr.
            while j<l:
                if t[j]=='1': # abbr starts here at j
                    k = j+1
                    while k<l and t[k]=='1':
                        k += 1
                    n = k-j # length of abbreviated chunk of string
                    abbr_word.append(n)
                    j = k
                else:
                    abbr_word.append(target[j])
                    j += 1
            abbr.append(abbr_word)
        
        # 2. sort the list
        abbr = sorted(abbr, key=len)
        
        # 3. iterate through the elements of the list and check, if valid abbr. found, return instantly.
        for abbr_word in abbr:
            if checkWord(abbr_word, dictionary, l):
                return ''.join(map(lambda x: str(x), abbr_word))