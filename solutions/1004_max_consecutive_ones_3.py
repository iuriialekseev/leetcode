class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = right = current = answer = 0

        while right < len(nums):
            if nums[right] == 0:
                current += 1

            while current > k:
                if nums[left] == 0:
                    current -= 1
                left += 1

            answer = max(answer, right - left + 1)
            right += 1

        return answer
