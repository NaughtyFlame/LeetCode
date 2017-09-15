class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = []
        res = 0
        while n:
            binary.append(n % 2)
            n /= 2
        while len(binary) < 32:
            binary.append(0)
            
        for index in range(32):
            res += binary[index]*2**(31-index)        
            
        return res
