class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum = n * (n + 1) // 2

        for num in nums:
            sum -= num

        return sum
