class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        mapping = {}
        
        for s in strs:
            temp = sorted(s)
            temp = "".join(temp)
            if temp in mapping:
                mapping[temp].append(s)
            else:
                mapping[temp] = [s]
            
        res = []
        for s, ar in mapping.items():
           res.append(ar)
        
        return res
        