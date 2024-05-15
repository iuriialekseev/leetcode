class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        output = []

        def backtrack(i):
            if i == length:
                output.append(nums[:])
                return

            for j in range(i, length):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return output
