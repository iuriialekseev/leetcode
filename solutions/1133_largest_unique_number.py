class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        result = -1
        for num, seen in dict.items():
            if seen == 1 and num > result:
                result = num

        return result
