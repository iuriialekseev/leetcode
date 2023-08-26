from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        keyword = "balloon"
        keyword_chars = defaultdict(int)
        for char in keyword:
            keyword_chars[char] += 1

        text_chars = defaultdict(int)
        for char in text:
            text_chars[char] += 1

        times = len(text) // len(keyword)
        for char, seen in keyword_chars.items():
            if text_chars[char] < seen:
                return 0

            times = min(times, text_chars[char] // seen)

        return times
