class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList = list(s)
        vowel = ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']
        vowel_List = []
        for index in range(len(strList)):
            if strList[index] in vowel:
                vowel_List.append(strList[index])
                strList[index] = "vowel"
                
        for index in range(len(strList)):
            if strList[index] == "vowel":
                strList[index] = vowel_List.pop()
        
        return "".join(strList)
