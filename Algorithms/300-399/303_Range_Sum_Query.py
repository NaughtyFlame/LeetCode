class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        len_array = len(nums)
        self._sumList = [None] * len_array
        if len_array != 0:
            self._sumList[0] = nums[0]
            
            for index in range(1, len_array):
                self._sumList[index] = self._sumList[index -1] +nums[index]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self._sumList[j]
        else:
            return self._sumList[j] - self._sumList[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
