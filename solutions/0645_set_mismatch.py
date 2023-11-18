class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1, -1]
        counts = [0] * (len(nums) + 1)

        for num in nums:
            counts[num] += 1

        for i in range(len(counts)):
            if counts[i] == 0:
                ans[1] = i
            if counts[i] == 2:
                ans[0] = i

        return ans
