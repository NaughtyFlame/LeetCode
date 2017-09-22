class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        if ransomNote != ransomNote.lower() or magazine != magazine.lower() or len(ransomNote) > len(magazine):
            return False
        
        for index in range(len(magazine)):
            if dict.has_key(magazine[index]):
                dict[magazine[index]] += 1
            else:
                dict[magazine[index]] = 1
                
        for index in range(len(ransomNote)):
            if dict.has_key(ransomNote[index]) and dict[ransomNote[index]] >= 1:
                dict[ransomNote[index]] -= 1
            else:
                return False
        
        return True
