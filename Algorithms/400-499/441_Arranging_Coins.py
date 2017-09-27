class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        low, high = 0, n
        
        while low <= high:
            mid = (low + high) / 2
            if (mid+1)*mid/2 > n:
                high = mid - 1
            else:
                low = mid + 1
        return high
