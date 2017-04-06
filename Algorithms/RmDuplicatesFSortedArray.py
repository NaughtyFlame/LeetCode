class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
        	return len(nums)
        else:
        	len_num = 0
        	for i in range(1,len(nums)):
				if nums[i] != nums [len_num]:
					len_num +=1
					nums[len_num] = nums[i] 
		return len_num + 1

mc = Solution()

print mc.removeDuplicates([1,1,2])
print mc.removeDuplicates([1,1,1,2,2,3])
print mc.removeDuplicates([1,2,2,3,3,3,3])
print mc.removeDuplicates([1])