class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n

            if candidate == n:
                count += 1
            else:
                count -= 1

        return candidate or -1
