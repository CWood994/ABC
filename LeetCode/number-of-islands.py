class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.explore(grid, i, j)
        return count
    
    def explore(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >=0 and j < len(grid[i]) and grid[i][j]=='1':
            grid[i][j] = 'x'
            
            # left
            self.explore(grid, i - 1, j)
            # right
            self.explore(grid, i + 1, j)
            # top
            self.explore(grid, i, j - 1)
            # bottom
            self.explore(grid, i, j + 1)
        
        
        