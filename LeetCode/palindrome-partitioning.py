class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        res = []
        self.helper(s, res, [])
        return res
        
        
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        
        for i in range(len(s)):
            if self.is_pal(s[:i+1]):
                self.helper(s[i+1:], res, path+[s[:i+1]])
        
    def is_pal(self, s):
        return s == s[::-1]