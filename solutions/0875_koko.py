import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_bph = 1
        max_bph = max(piles)

        while min_bph < max_bph:
            bph = (min_bph + max_bph) // 2

            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / bph)

            if hours <= h:
                max_bph = bph
            else:
                min_bph = bph + 1

        return max_bph
