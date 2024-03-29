import heapq


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        ans = 0

        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, cost)
            ans += cost

        return ans
