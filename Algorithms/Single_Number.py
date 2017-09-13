class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        filter = 0
        for num in nums:
            filter = filter ^ num
        return filter
