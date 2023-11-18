class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_i, i = 0, 0

        while i < len(nums):
            if nums[i] != val:
                nums[num_i] = nums[i]
                num_i += 1
            i += 1

        return num_i
