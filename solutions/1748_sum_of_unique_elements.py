from collections import defaultdict


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        sum = 0
        seen = defaultdict(int)

        for num in nums:
            if seen[num] == 0:
                sum += num
            elif seen[num] == 1:
                sum -= num

            seen[num] += 1

        return sum
