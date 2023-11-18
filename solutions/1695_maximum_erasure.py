class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right, curr, ans = 0, 0, 0, 0
        seen = set()

        while right < len(nums):
            if nums[right] not in seen:
                seen.add(nums[right])
                curr += nums[right]
                ans = max(ans, curr)
                right += 1
            else:
                seen.remove(nums[left])
                curr -= nums[left]
                left += 1

        return ans
