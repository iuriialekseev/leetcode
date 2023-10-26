from collections import defaultdict


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(combination, counter):
            if len(combination) == len(nums):
                result.append(list(combination))
                return

            for num in counter:
                if counter[num] > 0:
                    combination.append(num)
                    counter[num] -= 1
                    backtrack(combination, counter)
                    combination.pop()
                    counter[num] += 1

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        result = []
        backtrack([], counter)

        return result
