class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        path_count = []
        
        def run(grid,cur_path,row,col):
            cur_path += grid[row][col]
            print( row,col)
            while row!= len(grid)-1 and col!= len(grid[0])-1: 
                # move down
                if row!= len(grid)-1:
                    return run(grid,cur_path,row+1, col)
                # move right
                if col!= len(grid[0])-1:
                    return run(grid,cur_path,row, col+1)
            
            path_count.append(cur_path)
            return 
            
        run(grid,grid[0][0],0,0)
        return path_count

        


grid = [[1,3,1],[1,5,1],[4,2,1]]

obj = Solution()
print(obj.minPathSum(grid))