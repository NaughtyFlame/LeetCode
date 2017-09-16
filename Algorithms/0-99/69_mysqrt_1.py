class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		start = 1
		end = x 
		while start + 1 < end:
			mid = 0.5(start + end)
			if mid ** 2 == x:
				return mid
			elif mid ** 2 < x:
				start = mid
			else:
				end = mid
		if end ** 2 <= x:
			return end
		return start
