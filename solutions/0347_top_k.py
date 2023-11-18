from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heap.pop()

        return [num for _, num in heap]
