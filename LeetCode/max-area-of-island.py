class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        _max = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    _max = max(self.explore(grid, i, j), _max)
                    
        return _max
    
    def explore(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
            return 0
        
        count = 1
        grid[i][j] = 'x'
        
        # Top
        count += self.explore(grid, i, j+1)
        # Bottom
        count += self.explore(grid, i, j-1)
        # Left
        count += self.explore(grid, i-1, j)
        # Right
        count += self.explore(grid, i+1, j)
        
        return count
        