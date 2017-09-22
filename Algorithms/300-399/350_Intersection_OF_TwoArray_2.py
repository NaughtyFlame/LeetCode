class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = list()
        for num in nums1:
            if dict.has_key(num):
                dict[num] += 1
            else:
                dict[num] = 1
        
        for num in nums2:
            if dict.has_key(num) and dict[num] > 0:
                res.append(num)
                dict[num] -= 1
        
        return res
