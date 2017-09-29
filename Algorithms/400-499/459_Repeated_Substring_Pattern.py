class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(2, len(s)+1):
            if len(s) % i == 0:
                j = len(s) / i
                string = s[0:j]*i
                if s == string:
                    return True
                
        return False
