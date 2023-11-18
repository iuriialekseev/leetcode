class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
