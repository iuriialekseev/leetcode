from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = length = 0
        chars = defaultdict(int)

        while right < len(s):
            rc = s[right]
            chars[rc] += 1

            while chars[rc] > 1:
                lc = s[left]
                chars[lc] -= 1
                left += 1

            length = max(length, right - left + 1)
            right += 1

        return length
