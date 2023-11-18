from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1

        max_freq = max(freqs.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for char, freq in freqs.items():
            buckets[freq].append(char)

        ans = []
        for freq in range(len(buckets) - 1, 0, -1):
            for char in buckets[freq]:
                ans.append(char * freq)

        return "".join(ans)
