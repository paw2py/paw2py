Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col = len(grid[0]) # x axis of 2d grid
        row = len(grid)    # y axis of 2d grid
        
        def newland(rwy,clx):
            if 0 <= rwy < row and 0 <= clx < col and grid[rwy][clx] == '1':
                grid[rwy][clx] = '2'
                newland(rwy,clx-1) # left
                newland(rwy-1,clx) # top
                newland(rwy,clx+1) # right
                newland(rwy+1,clx) # bottom
                
            
        cnt_Ild = 0        
        for rw in range(row):
            for cl in range(col):
                if grid[rw][cl] == '1':
                    cnt_Ild += 1
                    #recursive fn to find neighbour land
                    newland(rw,cl)
        return cnt_Ild           
