class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index in range(len(numbers)):
            if dict.has_key(numbers[index]):
                result = []
                result.append(dict[numbers[index]])
                result.append(index+1)
                return result
            else:
                dict[target-numbers[index]] = index + 1
                
        return None
