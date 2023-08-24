class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) < k:
            return 0

        current = 0
        for i in range(k):
            current += nums[i]

        answer = current // k
        for i in range(k, len(nums)):
            current += nums[i]
            current -= nums[i - k]
            answer = max(answer, current // k)

        return answer
