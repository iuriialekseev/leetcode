class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid)
        h = len(grid[0])
        num = 0

        def traverse(x, y):
            if 0 <= x < w and 0 <= y < h and grid[x][y] == "1":
                grid[x][y] = '0'

                traverse(x + 1, y)
                traverse(x - 1, y)
                traverse(x, y + 1)
                traverse(x, y - 1)

        for x in range(w):
            for y in range(h):
                if grid[x][y] == '1':
                    num += 1
                    traverse(x, y)

        return num
