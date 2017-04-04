class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #首先建立对照表
        value = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
       	"""
		下面的参数解释：
		sum_temp 是缓存区的和，
		v_sum 是累加的和
		temp 是上一个字母的值
		基本算法是：
		如果 现在读到的数的值 和上一个相同，则加到缓存区
		如果 现在读到的数的值 比上一个数值大，则说明刚才是 大数左侧的数，所以缓存区的值为负
		如果 现在读到的数的值 比上一个数值小，则说明这是大数右边的数，需要左侧数加上右边，也就是说缓存区的值为正
       	"""
        sum_temp = 0
        v_sum = 0
        temp = s[0]
        for num in s:
        	if value[num] == temp:
        		sum_temp += value[num]
        	elif value[num] < temp:
        		v_sum += sum_temp
        		sum_temp = value[num]
        	else:
        		v_sum -= sum_temp
        		sum_temp = value[num]
        	temp = value[num]
        	#这里别忘了缓存区还有数，末尾的数都是需要加上的数。
        v_sum += sum_temp
        return v_sum

#test
mc = Solution()
print mc.romanToInt("MCCM") #1800
print mc.romanToInt("MCMLIV")    #1954
print mc.romanToInt("MMXIV") #2014 
print mc.romanToInt("MDLXX") #1570