class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        if num == 1:
            return True
        if num < 4:
            return False
        while low < high:
            mid = (low + high) / 2
            if mid ** 2 > num:
                high = mid - 1
            elif mid ** 2 < num:
                low = mid + 1
            else:
                return True
                
        return low ** 2 == num
