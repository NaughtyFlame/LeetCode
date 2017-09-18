class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        if len(nums) <= 1:
            return False
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
            
        return False
