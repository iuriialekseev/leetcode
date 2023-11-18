from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(bool)
        answer = []

        for num in nums1:
            seen[num] = True

        for num in nums2:
            if seen[num] == True:
                answer.append(num)
                seen[num] = False

        return answer
