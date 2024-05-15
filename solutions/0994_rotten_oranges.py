from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        queue = deque([])
        fresh = 0
        minutes = 0
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        for x in range(h):
            for y in range(w):
                if grid[x][y] == 2:
                    queue.append([x, y])
                if grid[x][y] == 1:
                    fresh += 1

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for xo, yo in moves:
                    xn, yn = x + xo, y + yo
                    if 0 <= xn < h and 0 <= yn < w and grid[xn][yn] == 1:
                        grid[xn][yn] = 2
                        fresh -= 1
                        queue.append([xn, yn])

        return -1 if fresh > 0 else minutes
