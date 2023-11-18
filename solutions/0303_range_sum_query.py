from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        self.sums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]
