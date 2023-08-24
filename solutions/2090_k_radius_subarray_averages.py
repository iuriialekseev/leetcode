class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        n = len(nums)
        window = 2 * k + 1
        averages = [-1] * n

        if window > n:
            return averages

        sum = 0
        for i in range(2 * k):
            sum += nums[i]

        for i in range(k, n - k):
            sum += nums[i + k]
            averages[i] = sum // window
            sum -= nums[i - k]

        return averages
