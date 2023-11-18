class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left

            if height[left] <= height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1

            max_area = max(area, max_area)

        return max_area
