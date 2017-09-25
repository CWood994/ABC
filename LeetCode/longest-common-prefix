class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) < 1:
            return ""
        
        cur = strs[0]
        
        for i in range(len(strs)):
            while cur != strs[i][0:len(cur)] and len(cur)>0:
                cur = cur[0:-1]
        
        return cur
        