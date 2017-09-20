class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list_pat = list(pattern)
        list_str = str.split()
        hash_pat = {}
        if pattern != pattern.lower() or str != str.lower() or len(list_pat) != len(list_str):
            return False
        
        for i in range(len(list_pat)):
            if hash_pat.has_key(list_pat[i]):
                if hash_pat[list_pat[i]] != list_str[i]:
                    return False
            else:
                if list_str[i] in hash_pat.values():
                    return False
                hash_pat[list_pat[i]] = list_str[i]
                    
        return True
