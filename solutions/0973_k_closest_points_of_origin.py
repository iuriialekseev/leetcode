import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for point in points:
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]
