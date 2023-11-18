from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        for i in range(len(s)):
            char = s[i]

            if counts[char] == 1:
                return i

        return -1

# s = "leetcode" => 0
# s = "loveleetcode" => 2
# s = "aabb" => -1
