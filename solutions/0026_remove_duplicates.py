class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq, i = 0, 0

        while i < len(nums):
            if nums[i] >= nums[uniq] and nums[i] != nums[uniq]:
                uniq += 1
                nums[uniq] = nums[i]
            i += 1

        return uniq + 1
