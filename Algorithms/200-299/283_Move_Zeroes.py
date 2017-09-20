class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                search_not_0 = True 
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        break
        return
