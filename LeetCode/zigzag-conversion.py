class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        cols = []
        for i in range(numRows):
            cols.append([])
        
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break
                cols[j].append(s[i])
                i += 1
                
            for j in range(numRows-2):
                if i >= len(s):
                    break
                cols[numRows - j - 2].append(s[i])
                i += 1
                
        s = ""
        for c in cols:
            s += "".join(c)
            
        return s
            