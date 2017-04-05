class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
        	return strs[0]
        elif len(strs) == 0:
        	return ""
        # find min_len in strs	
        last = 0
        minl = min([len(s) for s in strs])
        while last < minl:
        	for i in range(1,len(strs))
        		#注意 str[a] 与str[:a]的区别
        		if strs[0][last] != strs[i][last]:
        			return strs[0][:last]
        	last += 1
        return strs[0][last]


mc = Solution()
print mc.longestCommonPrefix(["a","b"])