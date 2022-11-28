class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        this solution completely works but this is not efficient in time complexity
        
        should consider a way to iterate over the grid from bottom up and replacing the values of the grid with the cost to the destination
        + excisting value.
        
        time complexity will be 0(m.n)
        
        this will be efficient than the recursive bruteforce method.
        
        see the screenshot
        '''
        height = len(grid)
        width =len(grid[0])
        
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if r == height-1 and c == width-1:
                    continue
                elif r == height-1:
                    grid[r][c] = grid[r][c] + grid[r][c+1]
                elif c == width-1:
                    grid[r][c] = grid[r][c] + grid[r+1][c]
                else:
                    grid[r][c] = min((grid[r][c] + grid[r+1][c]),(grid[r][c] + grid[r][c+1])) 
        return grid[0][0]


grid = [[1,3,1],[1,5,1],[4,2,1]]
grid1 =[[1,2,3],[4,5,6]]

obj = Solution()
print(obj.minPathSum(grid))