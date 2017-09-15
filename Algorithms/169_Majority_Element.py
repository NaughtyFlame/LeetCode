class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if dict.has_key(num):
                dict[num] += 1
            else:
                dict[num] = 1
        for n in dict.keys():
            if dict[n] > len(nums) / 2:
                return n
            
        return None
