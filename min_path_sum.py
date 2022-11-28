class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        this solution completely works but this is not efficient in time complexity
        
        should consider a way to 
        '''
        
        
        path_count = []
        
        
        
        def run(grid,cur_path,row,col):
            
            cur_path += grid[row][col]
            
            while row < len(grid)-1 or col < len(grid[0])-1: 
                # move down
                print(cur_path)
                if row < len(grid)-1:
                    run(grid,cur_path,row+1, col)
                # move right
                if col < len(grid[0])-1:
                    run(grid,cur_path,row, col+1)
                return
            if row == len(grid)-1 and col == len(grid[0])-1:
                print( row,col, cur_path)
                path_count.append(cur_path)
                return
            
        run(grid,0,0,0)
        print(path_count)
        return min(path_count)

        


grid = [[1,3,1],[1,5,1],[4,2,1]]
grid1 =[[1,2,3],[4,5,6]]

obj = Solution()
print(obj.minPathSum(grid1))