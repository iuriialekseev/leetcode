from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        result = 0
        for _, v in counts.items():
            if v > 1:
                result += v*(v-1)//2

        return result
