class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        sum = ""
        while indexa >= 0 or indexb >= 0:
        	if indexa >= 0:
        		x = int(a[indexa])
        	else:
        		x = 0
        	if indexb >= 0:
        		y = int(b[indexb])
        	else:
        		y = 0
        	if (x + y + carry) % 2 == 0:
        		sum = "0" + sum
        	else:
        		sum = "1" + sum
        	carry = (x + y + carry) / 2
        	indexa , indexb = indexa - 1 , indexb -1
        if carry == 1:
        	sum = '1' + sum
        return sum