# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
        mid = (high + low) / 2
        
        while low < high:
            if isBadVersion(mid):
                high = mid
            else:
                low = mid +1
            mid = (high + low) / 2
        return high
