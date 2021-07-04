class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        exit = [-1] * n

        for k in range(n):
            position = [0, k]
            while True:
                i = position[0]
                j = position[1]
                if (j == 0 and grid[i][0] == -1) or (j == n-1 and grid[i][-1] == 1):
                    break
                if grid[i][j] == 1 and grid[i][j+1] == 1:
                    position = [i+1, j+1]
                elif grid[i][j] == -1 and grid[i][j-1] == -1:
                    position = [i+1, j-1]
                else:
                    break
                if position[0] == m:
                    exit[k] = position[1]
                    break
        return exit
