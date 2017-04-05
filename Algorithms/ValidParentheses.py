class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = {
        	")" : "(",
        	"]" : "[",
        	"}" : "{"
        }
        #这道题用栈的方式实现，遍历字符串，检验到左括号入栈，检验到右括号时，出栈检验是否匹配，最后检验栈是否为空，排除右括号缺失的情况。        
        temp = []
        for char in s:
        	if char in check.values():
        		temp.append(char)
        	elif char in check.keys():
        		if len(temp) == 0:
        			return False
        		else:
        			if check[char] != temp.pop():
        				return False
        if len(temp) == 0:
        	return True
        else:
        	return False

#test
mc = Solution()
print mc.isValid("()")
print mc.isValid("((")
print mc.isValid("()[{}]")
print mc.isValid("([(]")
print mc.isValid("(](")
print mc.isValid("{[}")