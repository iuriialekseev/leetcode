class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]

            if curr == target:
                return mid
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
