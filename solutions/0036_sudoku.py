class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set()] * n
        cols = [set()] * n
        squares = [set()] * n

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r]:
                    return False

                rows[r].add(val)

                if val in cols[c]:
                    return False

                cols[c].add(val)

                square = (r // 3) * 3 + c // 3
                if val in squares[square]:
                    return False

                squares[square].add(val)

        return True
