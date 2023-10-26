class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = []
        for num in nums:
            if seen[num] is True:
                return True
            seen[num] = True

        return False
