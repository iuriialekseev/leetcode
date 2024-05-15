from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        start = max_count = max_length = 0

        for end in range(len(s)):
            counts[s[end]] += 1
            max_count = max(max_count, counts[s[end]])

            if end + 1 - start - max_count > k:
                counts[s[start]] -= 1
                start += 1

            max_length = end + 1 - start

        return max_length
