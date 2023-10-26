class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        progression = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if progression != arr[i] - arr[i - 1]:
                return False
        return True
