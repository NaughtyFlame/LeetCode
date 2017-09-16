class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if int(x) == x:
        	re = []
        	if x >= 0:
        		minus = 1
        		x = str(x)
        	else:
        		minus = (-1)
        		x = str(x * (-1))
        	for num in x:
        		re.insert(0,num)
        	x = int("".join(re))
        	#32bit integer overflow的上限值是2147483647
        	if x > 2147483647:
        		return 0
        	else:
        		return x * minus
        else:
        	return 0
#测试数据
mc1 = Solution()

print mc1.reverse(321)
print mc1.reverse(-312)
print mc1.reverse(1.25)
print mc1.reverse(150)
print mc1.reverse(1534236469)