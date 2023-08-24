class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = list(nums)
        left = 0
        right = len(nums) - 1
        index = right

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right = right - 1
            else:
                square = nums[left]
                left = left + 1

            result[index] = square * square
            index = index - 1

        return result
