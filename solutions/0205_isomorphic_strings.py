from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen_s = defaultdict(str)
        seen_t = defaultdict(str)

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]

            if seen_s[char_s] != "" and seen_s[char_s] != char_t:
                return False
            if seen_t[char_t] != "" and seen_t[char_t] != char_s:
                return False

            seen_s[char_s] = char_t
            seen_t[char_t] = char_s

        return True
