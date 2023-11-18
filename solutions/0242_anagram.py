from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        for char in t:
            counts[char] -= 1

        for count in counts.values():
            if count != 0:
                return False

        return True
