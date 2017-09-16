class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        else:
        	len_num = 0
        	for i in range(0,len(nums)):
        		if nums[i] != val:
        			nums[len_num] = nums[i]
        			len_num += 1
        	return len_num