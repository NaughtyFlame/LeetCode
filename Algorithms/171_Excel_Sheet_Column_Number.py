class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_list = list(s)
        result = 0
        index = 0
        while len(char_list) != 0:
            a = char_list.pop()
            result += (ord(a) - 64)*(26**index)
            index += 1
        return result
