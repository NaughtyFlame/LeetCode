class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        hex_map = '0123456789abcdef'
        res = ''
        for index in range(8):
            i = num & 15 # get last 4 num in binary
            c = hex_map[i]
            res = c + res
            num = num >> 4
        return res.lstrip('0') # remove leading zeroes
