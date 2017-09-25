class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for index in range(len(s)):
            if s[index] != t[index]:
                return t[index]
            
        return t[-1]
