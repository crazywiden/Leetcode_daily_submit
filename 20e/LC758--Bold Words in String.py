'''
Time complexity: O(n^2),44 ms,100.00%
Space complexity: O(1),14 MB,100.00%
'''
#method1: for loop
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        n = len(S)
        rec = [0] * n

        for word in words:
            p = 0
            while True:
                a = S.find(word, p)
                b = len(word)
                if a == -1:
                    break
                else:
                    rec[a:(a+b)]=[1]*b
                    p = a + 1
        res = ""
        i = 0
        while i < n:
            while i < n and rec[i] == 0:
                res += S[i]
                i += 1
            if i == n:
                break
            res += "<b>"
            while i < n and rec[i] == 1:
                res += S[i]
                i += 1
            res += "</b>"
        return res