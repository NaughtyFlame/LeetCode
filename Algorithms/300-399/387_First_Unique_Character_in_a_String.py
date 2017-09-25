class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        stack = []
        s = list(s)
        for index in range(len(s)):
            if dict.has_key(s[index]):
                dict[s[index]] = -1
            else:
                dict[s[index]] = index
                
        for value in dict.values():
            if value != -1:
                stack.append(value)
        stack.sort()
        if len(stack) > 0:
            return stack[0]
        else:
            return -1
