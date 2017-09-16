class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        else:
        	for i in range(0,len(nums)):
        		if target <= nums[i]:
        			return i
        	return len(nums)
