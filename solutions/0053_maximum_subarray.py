class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]

        for num in nums[1:]:
            max_current = max(num, num + max_current)
            max_global = max(max_current, max_global)

        return max_global
