class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_check = {}
        
        for index in range(len(nums)):
            if hash_check.has_key(nums[index]):
                if index - hash_check[nums[index]] <= k:
                    return True
                else:
                    hash_check[nums[index]] = index
            else:
                hash_check[nums[index]] = index
        return False
