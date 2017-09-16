class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
        	return "1"
        else:
        	last = self.countAndSay(n-1)
        	temp = "#"
        	CountSay = ""
        	count = 0
        	for s in last:
        		if s != temp:
        			if temp != "#":
        				CountSay += str(count) + temp
        			count = 1
        			temp = s
        		else:
        			count += 1
        	CountSay += str(count) + temp
        	return CountSay


mc = Solution()
print mc.countAndSay(1)
print mc.countAndSay(2)
print mc.countAndSay(3)
print mc.countAndSay(4)
print mc.countAndSay(5)
print mc.countAndSay(6)