class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = 1
        counter = 1
        n = n - 1
        while n >= 9 * counter * index:            
            n -= 9 * counter * index
            index += 1            
            counter = 10 ** (index - 1)
            
        return int(str(counter + n/index)[n%index])
