from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occs = defaultdict(int)
        for num in arr:
            occs[num] += 1

        freqs = defaultdict(int)
        for occ in occs.values():
            freqs[occ] += 1

        for freq in freqs.values():
            if freq > 1:
                return False

        return True
