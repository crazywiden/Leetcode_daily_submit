#reference：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/
'''
Time complexity: O(n), 40 ms, 96.30%
Space complexity: O(n), 13.9 MB, 5.51%
'''
#method1: stack
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        dict_t = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        l_tmp = []
        for i in s:
            l_tmp.insert(0,i)
            if len(l_tmp)<2: continue
            if l_tmp[1] not in dict_t: return False
            if dict_t[l_tmp[1]]==l_tmp[0]:
                l_tmp.pop(0)
                l_tmp.pop(0)
        return not l_tmp