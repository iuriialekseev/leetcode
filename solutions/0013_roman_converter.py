class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        subs = {
            "V": "I",
            "X": "I",
            "L": "X",
            "C": "X",
            "D": "C",
            "M": "C"
        }

        res = nums[s[0]]

        for i in range(1, len(s)):
            curr = s[i]
            prev = s[i-1]

            res += nums[curr]
            if curr in subs and subs[curr] == prev:
                res -= nums[prev] * 2

        return res
