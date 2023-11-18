class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        l = [0] * length
        r = [0] * length

        l[0] = 1
        for i in range(1, length):
            l[i] = nums[i - 1] * l[i - 1]

        r[-1] = 1
        for i in reversed(range(length - 1)):
            r[i] = nums[i + 1] * r[i + 1]

        ans = [0] * length
        for i in range(length):
            ans[i] = l[i] * r[i]

        return ans



Solution().productExceptSelf([1,2,3,4])
