class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                map[prev] = num

            stack.append(num)

        while stack:
            prev = stack.pop()
            map[prev] = -1

        res = []
        for num in nums1:
            res.append(map[num])

        return res
