import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for i in range(k):
            pile = -heapq.heappop(heap)
            remove = pile // 2
            heapq.heappush(heap, -(pile - remove))

        return -sum(heap)
