class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        statis = {}
        res = 0
        for char in s:
            if statis.has_key(char):
                statis[char] += 1
            else:
                statis[char] = 1
        record_single = False
        
        for times in statis.values():
            if times % 2 == 0:
                res += times
            elif record_single:
                res += times - 1
            else:
                record_single = True
                res += times 
                
        return res
    
    
"""
def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
"""
