from collections import defaultdict


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        seen = defaultdict(int)

        for num in arr:
            seen[num] += 1

        max_lucky = -1

        for num, count in seen.items():
            if num == count:
                max_lucky = max(max_lucky, num)

        return max_lucky
