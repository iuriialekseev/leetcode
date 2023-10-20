class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            if not valid(row, col) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            result = 0
            for x, y in directions:
                result = result + dfs(row + x, col + y)

            return 1 + result

        result = 0
        for row in range(rows):
            for col in range(cols):
                result = max(result, dfs(row, col))

        return result
