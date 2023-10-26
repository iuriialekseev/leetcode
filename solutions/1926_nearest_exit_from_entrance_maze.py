from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(maze), len(maze[0])
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        queue = deque()
        queue.append([start_row, start_col, 0])

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and maze[row][col] == "."

        def isExit(row, col):
            return row == 0 or row == rows - 1 or col == 0 or col == cols - 1

        while queue:
            row, col, steps = queue.popleft()

            for x, y in dirs:
                next_row, next_col = row + x, col + y
                if valid(next_row, next_col):
                    if isExit(next_row, next_col):
                        return steps + 1

                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, steps + 1])

        return -1
