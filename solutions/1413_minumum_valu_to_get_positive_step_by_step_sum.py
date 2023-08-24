class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        sum = minumum = 0
        for num in nums:
            sum += num
            minumum = min(minumum, sum)

        return 1 - minumum
