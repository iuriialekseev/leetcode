import heapq


class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        heapq.heapify(weight)
        capacity = 5000
        ans = 0

        while weight:
            item = heapq.heappop(weight)
            if capacity >= item:
                capacity -= item
                ans += 1
            else:
                break

        return ans
