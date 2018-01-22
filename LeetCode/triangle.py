class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        paths = [i for i in triangle[-1]]
        
        for level in reversed(range(len(triangle)-1)):
            for i in range(len(triangle[level])):
                paths[i] = min(paths[i], paths[i+1]) + triangle[level][i]
                
        return paths[0]
        