class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
        	return False
        a = list(str(x))
        m = []
        for i in range(len(a)):
        	m.append(a.pop())

        if str(x) == "".join(m):
        	return True
        else:
        	return False


#Test
mc = Solution()
print mc.isPalindrome(151)
print mc.isPalindrome(15788751)
print mc.isPalindrome(123)