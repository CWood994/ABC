class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            for j in range(i,len(haystack)):
                if len(needle) < j-i+1:
                    break
                if haystack[j] != needle[j-i]:
                    break
                if j-i == len(needle)-1:
                    return i
        return -1
         