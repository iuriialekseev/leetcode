from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = current

        for change in gain:
            current += change
            highest = max(highest, current)

        return highest
