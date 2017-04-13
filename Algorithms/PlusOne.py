class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(reversed(digits))
        digits[0] += 1
        carry, i = 0, 0
        while i < len(digits):
        	if digits[i] + carry == 10:
        		digits[i] = 0
        		carry = 1
        	else:
        		digits[i] += carry
        		carry = 0
        	i += 1
        if carry > 0:
            digits.append(1)
        return list(reversed(digits))

mc = Solution()
print mc.plusOne([9,9,9])
print mc.plusOne([1,2,3])
print mc.plusOne([8,9,9])