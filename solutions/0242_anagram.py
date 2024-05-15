from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)

        for ch in s:
            counts[ch] += 1

        for ch in t:
            counts[ch] -= 1

        for value in counts.values():
            if value != 0:
                return False

        return True
