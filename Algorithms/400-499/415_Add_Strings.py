class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j, carry = len(num1), len(num2), 0
        res = ""
        while i or j or carry:
            sum = 0
            if i > 0:
                sum += int(num1[i-1])
                i -= 1
            if j > 0:
                sum += int(num2[j-1])
                j -= 1
            sum += carry
            carry = sum / 10    
            res += str(sum % 10)
            
        return res[::-1]
