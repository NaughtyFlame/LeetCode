class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = []
        while n:
            char = chr(65 + (n-1) % 26)
            answer.insert(0, char)
            n = (n-1) / 26
        return "".join(answer)
