from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = defaultdict(int)

        for char in magazine:
            chars[char] += 1

        for char in ransomNote:
            if chars[char] == 0:
                return False
            chars[char] -= 1

        return True
