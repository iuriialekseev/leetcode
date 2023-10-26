def guess(num: int) -> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            elif result == -1:
                right = mid - 1

        return left
