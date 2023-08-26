class Solution:
    def countElements(self, arr: list[int]) -> int:
        nums = set(arr)
        sum = 0

        for num in arr:
            if num + 1 in nums:
                sum += 1

        return sum
