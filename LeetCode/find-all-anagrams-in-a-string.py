class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        
        counts = [0] * 256
        for c in p:
            counts[ord(c)] += 1
            
        lo = len(s)-1
        hi = lo
        
        
        while hi-lo+1 != len(p):
            counts[ord(s[lo])] -= 1
            lo -= 1
            
        counts[ord(s[lo])] -= 1           
        res = []
        while lo > -1:
            if all(x==0 for x in counts):
                res.append(lo)
            counts[ord(s[hi])] += 1
            hi -= 1
            lo -= 1
            counts[ord(s[lo])] -= 1
            
        return res
                