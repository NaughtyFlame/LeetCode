class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        three_max = []
        for num in nums:
            if num not in three_max:                
                if len(three_max) < 3:
                    three_max.append(num)
                elif num > min(three_max):
                    three_max.remove(min(three_max))
                    three_max.append(num)
        
        if len(three_max) == 0:
            return float('-inf')        
        elif len(three_max) < 3:
            return max(three_max)
        else:
            return min(three_max)
