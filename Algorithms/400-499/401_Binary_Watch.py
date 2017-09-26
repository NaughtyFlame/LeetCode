class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        stack = []
        
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    time = '%d:%02d' % (h, m)
                    stack.append(time)
                    
        return stack
