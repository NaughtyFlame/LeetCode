class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        ### TLE Solution
        if n <= 2:
            return 0
        nums = [i for i in range(2 , n)]
        i = 0
        x = 2
        while x <= int(n**0.5):
            x = nums[i]
            for index in nums[i + 1:]:
                if index % x == 0:
                    nums.remove(index)
            i += 1
        return len(nums)
        """    
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
