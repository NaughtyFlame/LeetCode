class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        sum = n
        while sum != 1:
            sum = 0
            while n:
                sum += (n % 10)**2
                n /= 10
            n = sum
            if sum not in stack:
                stack.append(sum)
            else:
                return False
        return True
