class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num

            if remainder in seen:
                return [seen[remainder], i]

            seen[num] = i

        return []
