class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        trig = [[1]]
        for i in range(numRows-1):
            trig.append([1,1])
            for j in range(i):
                trig[-1].insert(-1,trig[-2][j] + trig[-2][j+1])
                
        return trig
            