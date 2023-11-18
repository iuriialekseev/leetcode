class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique = set(nums)
        top_streak = 0

        for num in unique:
            if num - 1 not in unique:
                streak = 1
                curr = num

                while curr + 1 in unique:
                    streak += 1
                    curr += 1

                top_streak = max(streak, top_streak)

        return top_streak



Solution().longestConsecutive([1])
