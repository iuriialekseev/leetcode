from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        ans = 0

        for char in chars:
            counts[char] += 1

        for word in words:
            word_counts = defaultdict(int)
            for char in word:
                word_counts[char] += 1

            good = True
            for char, count in word_counts.items():
                if count > counts[char]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans
