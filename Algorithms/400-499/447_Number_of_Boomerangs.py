class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in points:
            hashmap = {}
            for j in points:
                x = i[0] - j[0]
                y = i[1] - j[1]
                distance = x*x + y*y
                if hashmap.has_key(distance):
                    hashmap[distance] += 1
                else:
                    hashmap[distance] = 1
                # hashmap[distance] = 1 + hashmap.get(distance, 0)
                # get函数 => 查找这个key，查找到就取值，未查找到，则返回0 (DEFAULT = None，这里设置为0)
                
            for k in hashmap.values():
                res += k*(k - 1)
        return res
