class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and ((n == 1) or (n % 2 == 0) and self.isPowerOfTwo(n/2))
