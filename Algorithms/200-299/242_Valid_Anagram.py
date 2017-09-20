class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s != s.lower() or t != t.lower() or len(s) != len(t):
            return False
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        return list_s == list_t
        
